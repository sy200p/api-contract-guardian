import argparse
from api_contract_guardian.loader import (load_json_file, validate_openapi_document)
from api_contract_guardian.comparator import compare_paths
import json

def main():
    parser = argparse.ArgumentParser(
        prog="api-contract-guardian",
        description="Detect Breaking Changes between OpenAPI contracts"
    )

    subparser = parser.add_subparsers(
        dest="command",
        required=True
    )

    compare_parser = subparser.add_parser(
        "compare",
        help="Compare two OpenAPI specifications."
    )

    compare_parser.add_argument(
        "--new",
        required=True,
        help="Path to the new OpenAPI specification."
    )

    compare_parser.add_argument(
        "--old",
        required=True,
        help="Path to the old OpenAPI specification."
    )

    args = parser.parse_args()
    try:
        old_spec = load_json_file(args.old)
        new_spec = load_json_file(args.new)

        validate_openapi_document(old_spec)
        validate_openapi_document(new_spec)

        changes = compare_paths(old_spec, new_spec)

        if not changes:
            print("No endpoint changes detected")
        else:
            print(f"Found {len(changes)} endpoint change(s):")
            for change in changes:
                print(
                    f"[{change['severity'].upper()}] "
                    f"{change['type']}: {change['path']} "
                )

       

    except FileNotFoundError:
        parser.error("One of the specified files does not exist")

    except json.JSONDecodeError as exc:
        parser.error(f"Invalid JSON: {exc}")

    except ValueError as exc:
        parser.error(str(exc))
    
    if __name__ == "__main__":
        main()