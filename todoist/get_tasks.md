python get_tasks.py [--project ID] [--filter FILTER] [--limit N]
--filter:str  Todoist filter syntax: "today" "p1" "#Work & overdue"
→ list of {id content priority project_id due labels description url}
! 4xx bad token/project_id
