from runtime_connector_handoff import dispatch_connector_request


def request(**updates):
    base = {
        "request_id": "REQ-P10-J-001",
        "operation": "update",
        "target": "provider-neutral-target",
        "payload": {"content": "bounded"},
        "authorized": True,
    }
    base.update(updates)
    return base


def test_authorization_and_identity_fail_closed_before_executor():
    calls = []

    def executor(payload):
        calls.append(payload)
        return {"status": "executed"}

    assert dispatch_connector_request(request(authorized=False), executor=executor)["reason"] == "AUTHORIZATION_REQUIRED"
    assert dispatch_connector_request(request(authorized="true"), executor=executor)["reason"] == "INVALID_AUTHORIZATION_SIGNAL"
    assert dispatch_connector_request(request(request_id=""), executor=executor)["reason"] == "MISSING_REQUEST_ID"
    assert calls == []


def test_malformed_payload_fails_closed_before_executor():
    calls = []
    result = dispatch_connector_request(request(payload="raw"), executor=lambda payload: calls.append(payload))
    assert result == {"status": "HOLD", "reason": "MALFORMED_PAYLOAD", "request_id": "REQ-P10-J-001"}
    assert calls == []


def test_valid_request_preserves_reported_connector_status_without_mutating_input():
    original = request()
    snapshot = {**original, "payload": dict(original["payload"])}

    def executor(payload):
        payload["payload"]["content"] = "executor-local-change"
        return {"status": "executed", "provider": "injected-test-double"}

    result = dispatch_connector_request(original, executor=executor)
    assert result["status"] == "RESULT_REPORTED"
    assert result["connector_status"] == "executed"
    assert result["connector_result"]["provider"] == "injected-test-double"
    assert original == snapshot


def test_partial_or_failure_status_is_reported_not_upgraded():
    for connector_status in ("partial_result", "authorization_failure", "external_rejection"):
        result = dispatch_connector_request(
            request(), executor=lambda payload, status=connector_status: {"status": status}
        )
        assert result["status"] == "RESULT_REPORTED"
        assert result["connector_status"] == connector_status


def test_missing_connector_status_becomes_unknown_not_success():
    result = dispatch_connector_request(request(), executor=lambda payload: {"detail": "ambiguous"})
    assert result["status"] == "EXECUTION_STATUS_UNKNOWN"
    assert result["reason"] == "MISSING_CONNECTOR_STATUS"


def test_executor_timeout_and_exception_do_not_become_success():
    def timeout(_payload):
        raise TimeoutError("test timeout")

    def crash(_payload):
        raise RuntimeError("test failure")

    assert dispatch_connector_request(request(), executor=timeout)["status"] == "TIMEOUT"
    result = dispatch_connector_request(request(), executor=crash)
    assert result["status"] == "EXECUTION_STATUS_UNKNOWN"
    assert result["error_type"] == "RuntimeError"
