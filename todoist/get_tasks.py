"""List active Todoist tasks. Usage: python get_tasks.py [--project ID] [--filter FILTER] [--limit N]"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import get, trim_task

def main():
    project_id = filter_str = limit = None
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--project" and i + 1 < len(args):
            project_id = args[i + 1]; i += 2
        elif args[i] == "--filter" and i + 1 < len(args):
            filter_str = args[i + 1]; i += 2
        elif args[i] == "--limit" and i + 1 < len(args):
            limit = int(args[i + 1]); i += 2
        else:
            print(f"ERROR: Unknown argument: {args[i]}"); sys.exit(1)

    data = get("/tasks", {"project_id": project_id, "filter": filter_str})
    tasks = data.get("results", []) if isinstance(data, dict) else data
    if limit:
        tasks = tasks[:limit]
    print(f"total={len(tasks)}")
    for t in tasks:
        t = trim_task(t)
        due = f" due:{t['due']}" if t.get("due") else ""
        print(f"{t['id']} p{t['priority']} {t['content']}{due}")
        if t.get("description"):
            print(f"  desc: {t['description']}")

if __name__ == "__main__":
    main()
