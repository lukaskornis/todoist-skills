# <arg>=required  [arg]=optional  →=returns  !=errors
python update_task.py <task_id> [--content TEXT] [--priority 1-4] [--due STRING] [--description TEXT] [--labels L1,L2]
task_id:str      Todoist task id (required)
--content:str    New task title
--priority:int   1=normal 2=medium 3=high 4=urgent
--due:str        Natural language due date e.g. "tomorrow" "every Mon"
--description:str  Task body / notes
--labels:str     Comma-separated label names (replaces existing labels)
→ {id content priority project_id due labels description}
! HTTP 404 if task not found  ! at least one flag required
