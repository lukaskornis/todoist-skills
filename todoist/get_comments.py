import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import get, require

def main():
    require(2, "python get_comments.py <task_id>")
    data = get("/comments", {"task_id": sys.argv[1]})
    comments = data.get("results", []) if isinstance(data, dict) else data
    print(f"total={len(comments)}")
    for c in comments:
        print(f"{c['id']} {c['posted_at']}: {c['content']}")

if __name__ == "__main__":
    main()
