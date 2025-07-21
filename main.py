import asyncio
import json
import uuid
from temporalio.client import Client
from workflows.json_workflow import JsonWorkflow


async def main():
    # Connect to Temporal
    client = await Client.connect("localhost:7233")

    # Load JSON from file
    with open("sample.json", "r") as f:
        data = json.load(f)

    # Generate a unique workflow ID
    workflow_id = f"json-workflow-{uuid.uuid4()}"

    # Start workflow execution
    result = await client.execute_workflow(
        JsonWorkflow.run,
        data,
        id=workflow_id,
        task_queue="json-task-queue",
    )

    print("✅ Pretty Printed JSON:\n", result)


if __name__ == "__main__":
    asyncio.run(main())
