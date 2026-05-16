"""Create a Todoist task. Usage: python create_task.py <content> [--project ID] [--priority 1-4] [--due STRING] [--description TEXT] [--labels L1,L2] [--parent ID]"""
import json, os, sys, urllib.request, urllib.error

_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
_BASE = "https://api.todoist.com/api/v1"

def _token():
    with open(os.path.join(_ROOT, "config.json")) as f:
        return json.load(f)["todoist_token"]

def _post(path, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"{_BASE}{path}", data=data,
        headers={"Authorization": f"Bearer {_token()}", "Content-Type": "application/json"}
    )
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
        "description": task.get("description") or "",
    }

def main():
    if len(sys.argv) < 2 or sys.argv[1].startswith("--"):
        print("ERROR: Usage: python create_task.py <content> [--project ID] [--priority 1-4] [--due STRING] [--description TEXT] [--labels L1,L2] [--parent ID]")
        sys.exit(1)

    content = sys.argv[1]
    payload = {"content": content}
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        flag = args[i]
        if i + 1 >= len(args):
            print(f"ERROR: Missing value for {flag}")
            sys.exit(1)
        val = args[i + 1]; i += 2
        if flag == "--project":
            payload["project_id"] = val
        elif flag == "--priority":
            payload["priority"] = int(val)
        elif flag == "--due":
            payload["due_string"] = val
        elif flag == "--description":
            payload["description"] = val
        elif flag == "--labels":
            payload["labels"] = [l.strip() for l in val.split(",")]
        elif flag == "--parent":
            payload["parent_id"] = val
        else:
            print(f"ERROR: Unknown flag: {flag}")
            sys.exit(1)

    print(json.dumps(_trim(_post("/tasks", payload)), indent=2))

if __name__ == "__main__":
    main()
