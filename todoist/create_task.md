# <arg>=required  [arg]=optional  →=returns  !=errors
python create_task.py <content> [--project ID] [--priority 1-4] [--due STRING] [--description TEXT] [--labels L1,L2] [--parent ID]
content:str      Task title (required)
--project:str    Project id (defaults to inbox)
--priority:int   1=normal 2=medium 3=high 4=urgent
--due:str        Natural language due date e.g. "tomorrow" "next Monday" "every day"
--description:str  Task description / body
--labels:str     Comma-separated label names
--parent:str     Parent task id (makes this a sub-task)
→ {id content priority project_id due description}
! HTTP 4xx if bad token, project_id, or parent_id
