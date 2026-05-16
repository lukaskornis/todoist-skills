"""Create a Todoist project. Usage: python create_project.py <name> [--color COLOR] [--parent ID] [--favorite]"""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import post, require

def _trim(p):
    return {
        "id": p["id"],
        "name": p["name"],
        "color": p.get("color"),
        "parent_id": p.get("parent_id"),
        "is_favorite": p.get("is_favorite", False),
        "is_inbox": p.get("inbox_project", False),
    }

def main():
    require(2, "python create_project.py <name> [--color COLOR] [--parent ID] [--favorite]")
    payload = {"name": sys.argv[1]}
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        flag = args[i]
        if flag == "--favorite":
            payload["is_favorite"] = True; i += 1; continue
        if i + 1 >= len(args):
            print(f"ERROR: Missing value for {flag}"); sys.exit(1)
        val = args[i + 1]; i += 2
        if flag == "--color":    payload["color"] = val
        elif flag == "--parent": payload["parent_id"] = val
        else:
            print(f"ERROR: Unknown flag: {flag}"); sys.exit(1)

    print(json.dumps(_trim(post("/projects", payload)), indent=2))

if __name__ == "__main__":
    main()
