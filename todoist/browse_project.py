"""Show a project overview: sections and tasks. Usage: python browse_project.py <project_id>"""
import sys, os, concurrent.futures
sys.path.insert(0, os.path.dirname(__file__))
from _lib import get, require

def _trim(task):
    due = task.get("due") or {}
    return {
        "id": task["id"],
        "content": task["content"],
        "priority": task["priority"],
        "due": due.get("string") or due.get("date") if isinstance(due, dict) else None,
        "description": task.get("description") or "",
        "parent_id": task.get("parent_id"),
        "section_id": task.get("section_id"),
    }

def _nest(tasks):
    by_id = {t["id"]: dict(t, subtasks=[]) for t in tasks}
    roots = []
    for t in by_id.values():
        pid = t.get("parent_id")
        if pid and pid in by_id:
            by_id[pid]["subtasks"].append(t)
        else:
            roots.append(t)
    return roots

def _print_task(t, indent="  "):
    due = f" due:{t['due']}" if t.get("due") else ""
    print(f"{indent}{t['id']} p{t['priority']} {t['content']}{due}")
    if t.get("description"):
        print(f"{indent}  desc: {t['description']}")
    for sub in t.get("subtasks", []):
        _print_task(sub, indent + "  ")

def main():
    require(2, "python browse_project.py <project_id>")
    project_id = sys.argv[1]

    with concurrent.futures.ThreadPoolExecutor() as pool:
        f_proj     = pool.submit(get, f"/projects/{project_id}")
        f_sections = pool.submit(get, "/sections", {"project_id": project_id})
        f_tasks    = pool.submit(get, "/tasks",    {"project_id": project_id})

    proj         = f_proj.result()
    raw_sections = (f_sections.result() or {}).get("results", [])
    raw_tasks    = (f_tasks.result()    or {}).get("results", [])

    section_map = {s["id"]: s["name"] for s in raw_sections}
    buckets = {None: []}
    for s in raw_sections:
        buckets[s["id"]] = []
    for t in raw_tasks:
        sid = t.get("section_id")
        if sid not in buckets:
            sid = None
        buckets[sid].append(_trim(t))

    top_level = sum(1 for t in raw_tasks if not t.get("parent_id"))
    print(f"{proj['id']} {proj['name']}  tasks={top_level}")
    for sid in [None] + [s["id"] for s in raw_sections]:
        tasks = _nest(buckets.get(sid, []))
        if not tasks:
            continue
        label = section_map.get(sid, "(no section)")
        print(f"[{label}]" + (f" id={sid}" if sid else ""))
        for t in tasks:
            _print_task(t)

if __name__ == "__main__":
    main()
