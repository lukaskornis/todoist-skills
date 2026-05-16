"""Show a project overview: sections and tasks. Usage: python browse_project.py <project_id>"""
import json, sys, os
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
    }

def _nest(tasks):
    """Return top-level tasks with subtasks nested under a 'subtasks' key."""
    by_id = {t["id"]: dict(t, subtasks=[]) for t in tasks}
    roots = []
    for t in by_id.values():
        pid = t.get("parent_id")
        if pid and pid in by_id:
            by_id[pid]["subtasks"].append(t)
        else:
            roots.append(t)
    # drop parent_id from output — redundant once nested
    def _clean(t):
        t.pop("parent_id", None)
        t["subtasks"] = [_clean(s) for s in t["subtasks"]]
        return t
    return [_clean(r) for r in roots]

def main():
    require(2, "python browse_project.py <project_id>")
    project_id = sys.argv[1]

    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor() as pool:
        f_proj     = pool.submit(get, f"/projects/{project_id}")
        f_sections = pool.submit(get, "/sections", {"project_id": project_id})
        f_tasks    = pool.submit(get, "/tasks",    {"project_id": project_id})

    proj         = f_proj.result()
    raw_sections = (f_sections.result() or {}).get("results", [])
    raw_tasks    = (f_tasks.result()    or {}).get("results", [])

    section_map = {s["id"]: s["name"] for s in raw_sections}
    section_map[None] = "(no section)"

    buckets = {None: []}
    for s in raw_sections:
        buckets[s["id"]] = []
    for t in raw_tasks:
        sid = t.get("section_id")
        if sid not in buckets:
            sid = None
        buckets[sid].append(_trim(t))

    top_level = sum(1 for t in raw_tasks if not t.get("parent_id"))
    sections_out = []
    for s in [None] + [s["id"] for s in raw_sections]:
        tasks = _nest(buckets.get(s, []))
        sections_out.append({
            "section": section_map[s],
            "section_id": s,
            "tasks": tasks,
        })

    print(json.dumps({
        "id": proj["id"],
        "name": proj["name"],
        "color": proj.get("color"),
        "is_favorite": proj.get("is_favorite", False),
        "task_count": top_level,
        "sections": sections_out,
    }, indent=2))

if __name__ == "__main__":
    main()
