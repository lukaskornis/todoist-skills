"""Shared Todoist API helpers. All HTTP errors exit(1) with 'ERROR: ...' on stdout."""
import json, os, sys, urllib.request, urllib.error, urllib.parse

_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
BASE = "https://api.todoist.com/api/v1"


def token():
    with open(os.path.join(_ROOT, "config.json")) as f:
        return json.load(f)["todoist_token"]


def _headers():
    return {"Authorization": f"Bearer {token()}"}


def _handle_error(e):
    if isinstance(e, urllib.error.HTTPError):
        print(f"ERROR: HTTP {e.code} — {e.read().decode()}")
    else:
        print(f"ERROR: {e}")
    sys.exit(1)


def get(path, params=None):
    url = f"{BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(url, headers=_headers())
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read())
    except Exception as e:
        _handle_error(e)


def post(path, payload=None, method="POST"):
    data = json.dumps(payload).encode() if payload else b""
    req = urllib.request.Request(
        f"{BASE}{path}", data=data, method=method,
        headers={**_headers(), "Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read()) if r.length else None
    except Exception as e:
        _handle_error(e)


def trim_task(task):
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


def require(n, usage):
    if len(sys.argv) < n:
        print(f"ERROR: Usage: {usage}")
        sys.exit(1)
