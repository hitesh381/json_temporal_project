from temporalio import workflow
import json

@workflow.defn
class JsonWorkflow:
    @workflow.run
    async def run(self, json_string: str) -> str:
        try:
            parsed = json.loads(json_string)
            pretty = json.dumps(parsed, indent=4)
            return pretty
        except json.JSONDecodeError:
            return "Invalid JSON provided"
