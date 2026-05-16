# <arg>=required  →=returns  !=errors
python create_section.py <project_id> <name>
project_id:str  Todoist project id
name:str        Section name
→ {id name project_id}
! HTTP 404 if project not found
