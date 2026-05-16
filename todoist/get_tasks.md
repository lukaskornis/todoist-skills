# <arg>=required  [arg]=optional  →=returns  !=errors
python get_tasks.py [--project PROJECT_ID] [--filter FILTER] [--limit N]
PROJECT_ID:str   Todoist project id
FILTER:str       Todoist filter string e.g. "today" "p1" "#Work & overdue"
N:int            Max tasks to return
→ list of {id content priority project_id due labels description url}
! HTTP 4xx if bad token or project_id
