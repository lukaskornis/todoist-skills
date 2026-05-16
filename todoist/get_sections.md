# <arg>=required  →=returns
python get_sections.py <project_id>
project_id:str  Todoist project id (get from get_projects)
→ list of {id name project_id section_order is_archived}
# Use returned id values as --section arg in move_task
