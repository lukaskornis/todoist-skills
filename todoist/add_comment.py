"""Post a comment on a task. Usage: python add_comment.py <task_id> <content>"""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import post, require

def main():
    require(3, "python add_comment.py <task_id> <content>")
    task_id, content = sys.argv[1], sys.argv[2]
    result = post("/comments", {"task_id": task_id, "content": content})
    print(json.dumps({
        "id": result["id"],
        "content": result["content"],
        "posted_at": result["posted_at"],
        "task_id": result["item_id"],
    }, indent=2))

if __name__ == "__main__":
    main()
