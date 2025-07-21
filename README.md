🚀 How to Run
****# Clone the repo or unzip this project****
cd json_temporal_project

# Create and activate Python virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install temporalio pytest pytest-asyncio

# Start Temporal Server in Docker (in another terminal)
docker run --rm -d -p 7233:7233 --name temporal temporalio/auto-setup

# Run the main app
python main.py
🧪 Running Unit Tests
pytest tests/

🧰 Project Structure

json_temporal_project/
├── main.py                     # CLI runner
├── sample.json                 # Input JSON
├── workflows/
│   └── json_workflow.py        # Temporal workflow definition
├── tests/
│   └── test_json_workflow.py   # Unit tests
└── README.md
