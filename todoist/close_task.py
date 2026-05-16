"""Mark a Todoist task complete. Usage: python close_task.py <task_id>"""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import post, require

def main():
    require(2, "python close_task.py <task_id>")
    task_id = sys.argv[1]
    post(f"/tasks/{task_id}/close")
    print(json.dumps({"closed": task_id}))

if __name__ == "__main__":
    main()
