# <arg>=required  →=returns  !=errors
python close_task.py <task_id>
task_id:str  Todoist task id
→ {closed: task_id}
! HTTP 404 if task not found  HTTP 401 if bad token
