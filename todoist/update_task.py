"""Update a Todoist task. Usage: python update_task.py <task_id> [--content TEXT] [--priority 1-4] [--due STRING] [--description TEXT] [--labels L1,L2]"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import post, trim_task, require

def main():
    require(2, "python update_task.py <task_id> [--content TEXT] [--priority 1-4] [--due STRING] [--description TEXT] [--labels L1,L2]")
    task_id = sys.argv[1]
    payload = {}
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        flag = args[i]
        if i + 1 >= len(args):
            print(f"ERROR: Missing value for {flag}"); sys.exit(1)
        val = args[i + 1]; i += 2
        if flag == "--content":       payload["content"] = val
        elif flag == "--priority":    payload["priority"] = int(val)
        elif flag == "--due":         payload["due_string"] = val
        elif flag == "--description": payload["description"] = val
        elif flag == "--labels":      payload["labels"] = [l.strip() for l in val.split(",")]
        else:
            print(f"ERROR: Unknown flag: {flag}"); sys.exit(1)

    if not payload:
        print("ERROR: Provide at least one field to update"); sys.exit(1)

    t = trim_task(post(f"/tasks/{task_id}", payload))
    due = f" due:{t['due']}" if t.get("due") else ""
    print(f"updated {t['id']} p{t['priority']} {t['content']}{due}")

if __name__ == "__main__":
    main()
