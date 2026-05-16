"""List comments on a task. Usage: python get_comments.py <task_id>"""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import get, require

def _trim(c):
    return {
        "id": c["id"],
        "content": c["content"],
        "posted_at": c["posted_at"],
        "posted_uid": c["posted_uid"],
        "reactions": c.get("reactions") or {},
    }

def main():
    require(2, "python get_comments.py <task_id>")
    task_id = sys.argv[1]
    data = get("/comments", {"task_id": task_id})
    comments = data.get("results", []) if isinstance(data, dict) else data
    print(json.dumps([_trim(c) for c in comments], indent=2))

if __name__ == "__main__":
    main()
