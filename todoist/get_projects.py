import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import get

def main():
    data = get("/projects")
    projects = data.get("results", data) if isinstance(data, dict) else data
    for p in projects:
        flags = (" inbox" if p.get("inbox_project") else "") + (" fav" if p.get("is_favorite") else "")
        print(f"{p['id']} {p['name']}{flags}")

if __name__ == "__main__":
    main()
