"""List sections in a project. Usage: python get_sections.py <project_id>"""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import get, require

def _trim(s):
    return {
        "id": s["id"],
        "name": s["name"],
        "project_id": s["project_id"],
        "section_order": s.get("section_order"),
        "is_archived": s.get("is_archived", False),
    }

def main():
    require(2, "python get_sections.py <project_id>")
    project_id = sys.argv[1]
    data = get("/sections", {"project_id": project_id})
    sections = data.get("results", []) if isinstance(data, dict) else data
    print(json.dumps([_trim(s) for s in sections], indent=2))

if __name__ == "__main__":
    main()
