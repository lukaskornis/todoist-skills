"""List active Todoist tasks. Usage: python get_tasks.py [--project PROJECT_ID] [--filter FILTER] [--limit N]"""
import json, os, sys, urllib.request, urllib.parse

_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
_BASE = "https://api.todoist.com/api/v1"

def _token():
    with open(os.path.join(_ROOT, "config.json")) as f:
        return json.load(f)["todoist_token"]

def _get(path, params=None):
    url = f"{_BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {_token()}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"ERROR: HTTP {e.code} — {e.read().decode()}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

def _trim(task):
    due = task.get("due") or {}
    return {
        "id": task["id"],
        "content": task["content"],
        "priority": task["priority"],
        "project_id": task["project_id"],
        "due": due.get("string") or due.get("date") if isinstance(due, dict) else None,
        "labels": task.get("labels") or [],
        "description": task.get("description") or "",
    }

def main():
    args = sys.argv[1:]
    project_id = None
    filter_str = None
    limit = None
    i = 0
    while i < len(args):
        if args[i] == "--project" and i + 1 < len(args):
            project_id = args[i + 1]; i += 2
        elif args[i] == "--filter" and i + 1 < len(args):
            filter_str = args[i + 1]; i += 2
        elif args[i] == "--limit" and i + 1 < len(args):
            limit = int(args[i + 1]); i += 2
        else:
            print(f"ERROR: Unknown argument: {args[i]}")
            sys.exit(1)

    data = _get("/tasks", {"project_id": project_id, "filter": filter_str})
    tasks = data.get("results", data) if isinstance(data, dict) else data
    if limit:
        tasks = tasks[:limit]
    print(json.dumps([_trim(t) for t in tasks], indent=2))

if __name__ == "__main__":
    main()
