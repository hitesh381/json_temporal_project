import asyncio
import json
from temporalio.client import Client
from workflows.json_workflow import JsonWorkflow

async def main():
    async with Client.connect("localhost:7233") as client:
        with open("sample.json", "r") as f:
            json_data = f.read()
        result = await client.execute_workflow(
            JsonWorkflow.run,
            json_data,
            id="json-workflow-id",
            task_queue="json-task-queue",
        )
        print("Workflow result:", result)

if __name__ == "__main__":
    asyncio.run(main())
