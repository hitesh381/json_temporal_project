# 🛠️ JSON Pretty Printer using Temporal

This project is a Python-based [Temporal](https://temporal.io) workflow that pretty-prints a JSON document passed via the CLI. It uses Temporal's local development setup with Docker Compose and is tested end-to-end.

---

## 📂 Features

- ✅ Temporal workflow in Python using `temporalio`
- ✅ CLI-based interface to pretty print JSON
- ✅ Temporal worker runs locally
- ✅ Temporal server + UI run via Docker Compose
- ✅ Clean project structure with unit tests

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/hitesh381/json_temporal_project.git
cd json_temporal_project
```

---

### 2️⃣ Setup Python Environment

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

---

### 3️⃣ Start Temporal Server and UI

```bash
docker-compose up -d
```

- Temporal gRPC: `localhost:7233`
- Web UI: [http://localhost:8080](http://localhost:8080)

---

### 4️⃣ Start the Temporal Worker (from host)

```bash
python worker_runner.py
```

You should see:
```bash
🚀 Worker started on 'json-task-queue'...
```

---

### 5️⃣ Run the Main CLI to Trigger Workflow

```bash
python main.py sample.json
```

You should see pretty-printed output like:

```✅ Pretty Printed JSON:
 [
    {
        "age": 30,
        "name": "Alice"
    },
    {
        "age": 25,
        "name": "Bob"
    }
]
```

---

## 🧪 Run Unit Tests

```bash
PYTHONPATH=. pytest tests/
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
=============================================================================== test session starts ===============================================================================
platform linux -- Python 3.8.10, pytest-8.3.5, pluggy-1.5.0
rootdir: /root/json_temporal_project
plugins: asyncio-0.24.0
asyncio: mode=strict, default_loop_scope=None
collected 2 items                                                                                                                                                                 

tests/test_json_workflow.py ..                                                                                                                                              [100%]

================================================================================ 2 passed in 0.10s ================================================================================
```

---

## 🧰 Project Structure

```bash
json_temporal_project/
├── main.py                 # CLI runner that starts the workflow
├── worker_runner.py        # Starts Temporal worker on task queue
├── workflows/
│   └── json_workflow.py    # Workflow definition
├── sample.json             # Sample JSON input (list of dicts)
├── tests/
│   └── test_json_workflow.py  # Unit tests
├── requirements.txt        # Python dependencies
├── Dockerfile              # (Optional) For containerizing worker
└── docker-compose.yml      # Starts Temporal server + UI
```

---

## 🌐 Temporal UI

You can observe the workflow state via the UI at:  
🔗 [http://localhost:8080](http://localhost:8080)

Look for:
- Namespace: `default`
- Workflow Type: `JsonWorkflow`
- Status: Running / Completed / Failed

---

## ✅ Summary

| Component         | Method             | Location         |
|------------------|--------------------|------------------|
| Temporal Server   | Docker Compose     | `localhost:7233` |
| Temporal UI       | Docker Compose     | `localhost:8080` |
| Worker            | Python script      | `worker_runner.py` |
| CLI client        | Python script      | `main.py`        |

---

## 📌 Notes

- You can extend this by Dockerizing the worker too.
- The current setup allows fast dev iteration from host.
- Compatible with Mac, Linux, WSL.

---

## 💡 Future Enhancements (Optional)

- Add a Dockerized CLI/worker for full Compose-based orchestration
- Add Helm or KIND manifests for Kubernetes deployment
- CI/CD with GitHub Actions
