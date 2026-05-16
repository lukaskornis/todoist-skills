"""Create a Todoist task. Usage: python create_task.py <content> [--project ID] [--priority 1-4] [--due STRING] [--description TEXT] [--labels L1,L2] [--parent ID]"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import post, trim_task, require

def main():
    require(2, "python create_task.py <content> [--project ID] [--priority 1-4] [--due STRING] [--description TEXT] [--labels L1,L2] [--parent ID]")
    payload = {"content": sys.argv[1]}
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        flag = args[i]
        if i + 1 >= len(args):
            print(f"ERROR: Missing value for {flag}"); sys.exit(1)
        val = args[i + 1]; i += 2
        if flag == "--project":       payload["project_id"] = val
        elif flag == "--priority":    payload["priority"] = int(val)
        elif flag == "--due":         payload["due_string"] = val
        elif flag == "--description": payload["description"] = val
        elif flag == "--labels":      payload["labels"] = [l.strip() for l in val.split(",")]
        elif flag == "--parent":      payload["parent_id"] = val
        else:
            print(f"ERROR: Unknown flag: {flag}"); sys.exit(1)

    t = trim_task(post("/tasks", payload))
    due = f" due:{t['due']}" if t.get("due") else ""
    print(f"{t['id']} p{t['priority']} {t['content']}{due}")

if __name__ == "__main__":
    main()
