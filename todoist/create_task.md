python create_task.py <content> [--project ID] [--priority 1-4] [--due STRING] [--description TEXT] [--labels L1,L2] [--parent ID]
--priority  1=normal 2=medium 3=high 4=urgent
--due:str   natural language: "tomorrow" "next Monday" "every day"
--labels:str  comma-separated; --parent ID makes it a subtask
→ {id content priority project_id due description}
! 4xx bad token/project_id/parent_id
