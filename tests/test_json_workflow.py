import pytest
import json
from workflows.json_workflow import JsonWorkflow

@pytest.mark.asyncio
async def test_valid_json():
    workflow = JsonWorkflow()
    input_data = [{"name": "Test", "age": 99}]
    result = await workflow.run(input_data)
    assert '"name": "Test"' in result
    assert json.loads(result)[0]["age"] == 99

@pytest.mark.asyncio
async def test_empty_list():
    workflow = JsonWorkflow()
    input_data = []
    result = await workflow.run(input_data)
    assert result == "[]"
