import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import post, require

def main():
    require(3, "python add_comment.py <task_id> <content>")
    r = post("/comments", {"task_id": sys.argv[1], "content": sys.argv[2]})
    print(f"comment {r['id']}")

if __name__ == "__main__":
    main()
