# API Contract Guardian

API Contract Guardian is a small Python project that helps detect breaking changes between OpenAPI contract versions. It compares an older API specification with a newer one and reports changes such as removed or newly added endpoints. This is useful when teams update backend APIs and want to check whether the new contract is backward compatible.

## What this project does

The project:

- loads two OpenAPI JSON files
- validates that each file is a valid OpenAPI document
- compares the `paths` section between the old and new versions
- prints any endpoint changes with a severity level

This makes it easier to quickly review API evolution before deploying a new contract.

## Setup a virtual environment

From the project root, create and activate a virtual environment:

```bash
cd api-contract-guardian
python3.11 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
cd api-contract-guardian
python -m venv .venv
.\ .venv\Scripts\Activate.ps1
```

Then install the project in editable mode:

```bash
python -m pip install --upgrade pip
pip install -e .
```

## Running the project

The repository includes example OpenAPI files in the `examples/` folder, so you can test it with:

```bash
api-contract-guardian compare --old examples/old.json --new examples/new.json
```

This will compare the old and new contract files and print any detected endpoint changes.

## Example output

```bash
Found 1 endpoint change(s):
[BREAKING] endpoint_removed: /users/{id}
```

## Project structure

- `src/api_contract_guardian/` - Python package
- `examples/` - sample OpenAPI JSON files
- `pyproject.toml` - Python package configuration

## Requirements

- Python 3.11+
- `pip`
- OpenAPI JSON files in a valid contract format
