from temporalio import workflow
import json


@workflow.defn
class JsonWorkflow:
    @workflow.run
    async def run(self, data: dict) -> str:
        return json.dumps(data, indent=4)
