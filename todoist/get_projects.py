"""List Todoist projects. Usage: python get_projects.py"""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import get

def _trim(p):
    return {
        "id": p["id"],
        "name": p["name"],
        "is_inbox": p.get("inbox_project", False),
        "is_favorite": p.get("is_favorite", False),
        "color": p.get("color"),
        "parent_id": p.get("parent_id"),
    }

def main():
    data = get("/projects")
    projects = data.get("results", data) if isinstance(data, dict) else data
    print(json.dumps([_trim(p) for p in projects], indent=2))

if __name__ == "__main__":
    main()
