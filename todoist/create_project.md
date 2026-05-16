# <arg>=required  [arg]=optional  →=returns  !=errors
python create_project.py <name> [--color COLOR] [--parent ID] [--favorite]
name:str       Project name (required)
--color:str    Color name: red orange yellow green teal charcoal (default: charcoal)
--parent:str   Parent project id (creates a sub-project)
--favorite      Mark as favourite
→ {id name color parent_id is_favorite is_inbox}
! HTTP 400 if invalid color
