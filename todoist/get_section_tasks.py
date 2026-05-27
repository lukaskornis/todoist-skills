"""List active tasks in a section. Usage: python get_section_tasks.py <section_id>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import get, trim_task, require

def main():
    require(2, "get_section_tasks.py <section_id>")
    section_id = sys.argv[1]

    data = get("/tasks", {"section_id": section_id})
    tasks = data.get("results", []) if isinstance(data, dict) else data
    print(f"total={len(tasks)}")
    for t in tasks:
        t = trim_task(t)
        due = f" due:{t['due']}" if t.get("due") else ""
        print(f"{t['id']} p{t['priority']} {t['content']}{due}")
        if t.get("description"):
            print(f"  desc: {t['description']}")

if __name__ == "__main__":
    main()
