# Assistant Team NN

## 1. Project Overview

This project develops a virtual assistant using Python.

The project is organized into separate components for the assistant logic, user interface, data, tests, documentation, and project scripts.

## 2. Project Structure

```text
assistant-teamNN/
├── README.md
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── src/
│   └── assistant/
│       └── __init__.py
├── ui/
├── data/
├── tests/
├── docs/
└── scripts/
    └── check_env.py
```

## 3. Requirements

- Python 3.10 or newer
- Git
- pip
- virtual environment (`venv`)

## 4. Setup

Clone the repository:

```bash
git clone https://github.com/htvtuong2534-lab/assistantgroup8.git
cd assistant-teamNN
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## 5. Check the Environment

Run:

```bash
python scripts/check_env.py
```

The script checks whether the Python environment is ready for the project.

## 6. Running the Project

The project entry point and running instructions will be updated when the main assistant functionality is implemented.

## 7. Testing

Tests will be stored in the `tests/` directory.

Run tests with:

```bash
pytest
```

## 8. Team

See [docs/team.md](docs/team.md) for team members and responsibilities.