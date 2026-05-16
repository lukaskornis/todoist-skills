import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import post, require

def main():
    require(3, "python create_section.py <project_id> <name>")
    s = post("/sections", {"project_id": sys.argv[1], "name": sys.argv[2]})
    print(f"{s['id']} {s['name']}")

if __name__ == "__main__":
    main()
