"""Show a project overview: sections and tasks. Usage: python browse_project.py <project_id>"""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import get, trim_task, require

def main():
    require(2, "python browse_project.py <project_id>")
    project_id = sys.argv[1]

    # Fetch project, sections, and tasks in parallel using threads for speed
    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor() as pool:
        f_proj     = pool.submit(get, f"/projects/{project_id}")
        f_sections = pool.submit(get, "/sections", {"project_id": project_id})
        f_tasks    = pool.submit(get, "/tasks",    {"project_id": project_id})

    proj = f_proj.result()
    raw_sections = (f_sections.result() or {}).get("results", [])
    raw_tasks    = (f_tasks.result()    or {}).get("results", [])

    section_map = {s["id"]: s["name"] for s in raw_sections}
    section_map[None] = "(no section)"

    # Group tasks by section
    buckets = {None: []}
    for s in raw_sections:
        buckets[s["id"]] = []
    for t in raw_tasks:
        sid = t.get("section_id")
        if sid not in buckets:
            sid = None
        buckets[sid].append(trim_task(t))

    sections_out = []
    for s in [None] + [s["id"] for s in raw_sections]:
        tasks = buckets.get(s, [])
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
        "task_count": len(raw_tasks),
        "sections": sections_out,
    }, indent=2))

if __name__ == "__main__":
    main()
