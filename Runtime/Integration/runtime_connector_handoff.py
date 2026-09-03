"""Provider-neutral Runtime connector handoff for the bounded Gate-13 seam.

The handoff validates a Runtime outbound request and delegates only through a
caller-supplied executor. It does not import or authenticate any provider.
Connector results are reported without converting a request into success.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Callable


def _hold(reason: str, *, request_id: str | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"status": "HOLD", "reason": reason}
    if request_id:
        result["request_id"] = request_id
    return result


def dispatch_connector_request(
    request: dict[str, Any],
    *,
    executor: Callable[[dict[str, Any]], Any],
) -> dict[str, Any]:
    """Validate and dispatch one provider-neutral external request.

    Local validation proves only the Runtime/interface handoff contract. The
    injected executor owns provider-specific authentication, transport and the
    truth of the execution result it returns.
    """
    if not isinstance(request, dict):
        return _hold("INVALID_REQUEST")

    request_id = request.get("request_id")
    operation = request.get("operation")
    target = request.get("target")
    for value, reason in (
        (request_id, "MISSING_REQUEST_ID"),
        (operation, "MISSING_OPERATION"),
        (target, "MISSING_TARGET"),
    ):
        if not isinstance(value, str) or not value.strip():
            return _hold(reason, request_id=request_id if isinstance(request_id, str) else None)

    authorized = request.get("authorized")
    if type(authorized) is not bool:
        return _hold("INVALID_AUTHORIZATION_SIGNAL", request_id=request_id)
    if authorized is not True:
        return _hold("AUTHORIZATION_REQUIRED", request_id=request_id)

    payload = request.get("payload")
    if not isinstance(payload, dict):
        return _hold("MALFORMED_PAYLOAD", request_id=request_id)

    if not callable(executor):
        return _hold("EXECUTOR_UNAVAILABLE", request_id=request_id)

    dispatch_request = {
        "request_id": request_id.strip(),
        "operation": operation.strip(),
        "target": target.strip(),
        "payload": deepcopy(payload),
    }

    try:
        connector_result = executor(deepcopy(dispatch_request))
    except TimeoutError:
        return {
            "status": "TIMEOUT",
            "request_id": request_id,
            "operation": operation,
            "target": target,
        }
    except Exception as exc:  # connector failures must not become optimistic success
        return {
            "status": "EXECUTION_STATUS_UNKNOWN",
            "reason": "EXECUTOR_EXCEPTION",
            "error_type": type(exc).__name__,
            "request_id": request_id,
            "operation": operation,
            "target": target,
        }

    if not isinstance(connector_result, dict):
        return {
            "status": "EXECUTION_STATUS_UNKNOWN",
            "reason": "MALFORMED_CONNECTOR_RESULT",
            "request_id": request_id,
            "operation": operation,
            "target": target,
        }

    connector_status = connector_result.get("status")
    if not isinstance(connector_status, str) or not connector_status.strip():
        return {
            "status": "EXECUTION_STATUS_UNKNOWN",
            "reason": "MISSING_CONNECTOR_STATUS",
            "request_id": request_id,
            "operation": operation,
            "target": target,
            "connector_result": deepcopy(connector_result),
        }

    return {
        "status": "RESULT_REPORTED",
        "request_id": request_id,
        "operation": operation,
        "target": target,
        "connector_status": connector_status,
        "connector_result": deepcopy(connector_result),
    }
