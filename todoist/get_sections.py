import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import get, require

def main():
    require(2, "python get_sections.py <project_id>")
    data = get("/sections", {"project_id": sys.argv[1]})
    sections = data.get("results", []) if isinstance(data, dict) else data
    for s in sections:
        print(f"{s['id']} {s['name']}")

if __name__ == "__main__":
    main()
