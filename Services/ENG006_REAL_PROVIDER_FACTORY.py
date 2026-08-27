"""Fail-closed construction of the existing governed GitHub connector."""
from Services.GITHUB_REPOSITORY_CONNECTOR import GitHubConnectorConfig, GitHubRepositoryConnector


def build_real_eng006_consumer():
    config = GitHubConnectorConfig.from_environment()
    connector = GitHubRepositoryConnector(config)

    def consume(candidate):
        from Services.ENG006_SRV009_PRODUCTION_ADAPTER import ProductionExecutionCandidate, execute_update
        execution = ProductionExecutionCandidate(
            execution_id=candidate["execution_id"],
            task_id=candidate["task_id"],
            session_id=candidate["session_id"],
            source_trace_id=candidate["source_trace_id"],
            path=candidate["path"],
            content=candidate["content"],
            purpose=candidate["purpose"],
            necessity_evidence=candidate["necessity_evidence"],
            commit_message=candidate["commit_message"],
            authorized=candidate["authorization_status"] == "AUTHORIZED",
        )
        return execute_update(execution, connector=connector)

    return consume
