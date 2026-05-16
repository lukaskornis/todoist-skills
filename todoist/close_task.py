import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _lib import post, require

def main():
    require(2, "python close_task.py <task_id>")
    post(f"/tasks/{sys.argv[1]}/close")
    print(f"closed {sys.argv[1]}")

if __name__ == "__main__":
    main()
