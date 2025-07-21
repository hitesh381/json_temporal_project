# JSON Temporal Project

A Python project demonstrating Temporal workflow orchestration for JSON data processing.

## Prerequisites

- Python 3.7+
- Docker
- Git

## How to Run 🚀

### 1. Clone the Repository

```bash
git clone https://github.com/hitesh381/json_temporal_project.git
cd json_temporal_project
```

### 2. Create and Activate Python Virtual Environment

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install temporalio pytest pytest-asyncio
```

### 4. Start Temporal Server in Docker

Open a new terminal and run:

```bash
docker run --rm -d -p 7233:7233 --name temporal temporalio/auto-setup
```

### 5. Run the Main Application

```bash
python main.py
```

## 🧪 Running Unit Tests

```bash
pytest tests/
```

## 🧰 Project Structure

```
json_temporal_project/
├── main.py                    # CLI runner
├── sample.json               # Input JSON data
├── workflows/
│   └── json_workflow.py      # Temporal workflow definition
├── tests/
│   └── test_json_workflow.py # Unit tests
└── README.md                 # Project documentation
```

## Features

- Temporal workflow orchestration
- JSON data processing
- Unit testing with pytest
- Docker-based Temporal server setup

## Technologies Used

- **Temporal**: Workflow orchestration
- **Python**: Core programming language
- **Docker**: Containerized Temporal server
- **Pytest**: Testing framework
