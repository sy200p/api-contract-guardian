from typing import Any

def compare_paths(old_spec: dict[str, Any],new_spec: dict[str, Any])-> list[dict[str, str]]: 
    changes: list[dict[str, str]] = []

    old_paths = old_spec["paths"]
    new_paths = new_spec["paths"]

    http_methods = {
        "get","post","put","patch","delete","options","head","trace"
    }

    for path in new_paths:
        if path not in old_paths:
            changes.append({
                "type": "endpoint_added",
                "path": path,
                "severity":"info"
            })
            continue
        
    for path in old_paths:
        if path not in new_paths:
            changes.append({
                "type":"endpoint_removed",
                "path":path,
                "severity":"breaking"
            })
    return changes