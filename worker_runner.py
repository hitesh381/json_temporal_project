import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from workflows.json_workflow import JsonWorkflow


async def main():
    client = await Client.connect("localhost:7233")

    # Register worker
    worker = Worker(
        client,
        task_queue="json-task-queue",
        workflows=[JsonWorkflow],
    )

    print("🚀 Worker started on 'json-task-queue'...")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
