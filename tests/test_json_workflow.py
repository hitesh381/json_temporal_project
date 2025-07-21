import asyncio
import pytest
from workflows.json_workflow import JsonWorkflow

@pytest.mark.asyncio
async def test_valid_json():
    workflow = JsonWorkflow()
    input_json = '[{"name": "Test", "age": 99}]'
    result = await workflow.run(input_json)
    assert '"name": "Test"' in result
    assert '"age": 99' in result

@pytest.mark.asyncio
async def test_invalid_json():
    workflow = JsonWorkflow()
    input_json = '{"invalid"}'
    result = await workflow.run(input_json)
    assert result == "Invalid JSON provided"
