# <arg>=required  [arg]=optional  →=returns  !=errors
python move_task.py <task_id> [--section ID] [--project ID] [--parent ID]
task_id:str    Todoist task id (required)
--section:str  Move into this section id (get from get_sections)
--project:str  Move to this project id (get from get_projects); clears section
--parent:str   Make a subtask of this task id; moves to same project automatically
→ {id content priority project_id due labels description}
! At least one flag required  ! HTTP 404 if ids not found
# To move out of a section back to project root: use --project with same project id
