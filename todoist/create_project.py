import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import post, require

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

    p = post("/projects", payload)
    print(f"{p['id']} {p['name']}")

if __name__ == "__main__":
    main()
