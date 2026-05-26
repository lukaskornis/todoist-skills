python update_task.py <task_id> [--content TEXT] [--priority 1-4] [--due STRING] [--description TEXT] [--labels L1,L2]
--priority  1=normal 2=medium 3=high 4=urgent
--due:str   natural language: "tomorrow" "every Mon"
--labels:str  comma-separated; replaces existing labels
→ {id content priority project_id due labels description}
! 404  at least one flag required
