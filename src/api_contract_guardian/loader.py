import json
from pathlib import Path
from typing import Any

def load_json_file(file_path:str)->dict[str,Any]:
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("OpenAPI document must be a JSON object.")
    
    return data


def validate_openapi_document(data: dict[str, Any]) -> None:
    if "openapi" not in data:
        raise ValueError("Missing required field: 'openapi'")

    if "info" not in data:
        raise ValueError("Missing required field: 'info'")

    if "paths" not in data:
        raise ValueError("Missing required field: 'paths'")

    if not isinstance(data["info"], dict):
        raise ValueError("'info' must be a JSON object")

    if not isinstance(data["paths"], dict):
        raise ValueError("'paths' must be a JSON object")

    if "title" not in data["info"]:
        raise ValueError("Missing required field: 'info.title'")

    if "version" not in data["info"]:
        raise ValueError("Missing required field: 'info.version'")

    