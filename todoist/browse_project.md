# <arg>=required  →=returns  !=errors
python browse_project.py <project_id>
project_id:str  Todoist project id (get from get_projects)
→ {id name color is_favorite task_count sections:[{section section_id tasks:[...]}]}
# Tasks are grouped by section; unsectioned tasks appear under "(no section)"
# Use get_projects to find project ids
! HTTP 404 if project not found
