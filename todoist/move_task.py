"""Move a task to a different section, project, or parent. Usage: python move_task.py <task_id> [--section ID] [--project ID] [--parent ID]"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import post, trim_task, require

def main():
    require(2, "python move_task.py <task_id> [--section ID] [--project ID] [--parent ID]")
    task_id = sys.argv[1]
    payload = {}
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        flag = args[i]
        if i + 1 >= len(args):
            print(f"ERROR: Missing value for {flag}"); sys.exit(1)
        val = args[i + 1]; i += 2
        if flag == "--section":    payload["section_id"] = val
        elif flag == "--project":  payload["project_id"] = val
        elif flag == "--parent":   payload["parent_id"] = val
        else:
            print(f"ERROR: Unknown flag: {flag}"); sys.exit(1)

    if not payload:
        print("ERROR: Provide --section, --project, or --parent"); sys.exit(1)

    t = trim_task(post(f"/tasks/{task_id}/move", payload))
    dest = " ".join(f"{k}={v}" for k, v in payload.items())
    print(f"moved {t['id']} {dest}")

if __name__ == "__main__":
    main()
