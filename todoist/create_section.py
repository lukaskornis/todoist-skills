"""Create a section in a project. Usage: python create_section.py <project_id> <name>"""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import post, require

def main():
    require(3, "python create_section.py <project_id> <name>")
    project_id, name = sys.argv[1], sys.argv[2]
    s = post("/sections", {"project_id": project_id, "name": name})
    print(json.dumps({
        "id": s["id"],
        "name": s["name"],
        "project_id": s["project_id"],
    }, indent=2))

if __name__ == "__main__":
    main()
