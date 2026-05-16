# <arg>=required  →=returns
python get_comments.py <task_id>
task_id:str  Todoist task id
→ list of {id content posted_at posted_uid reactions}
# reactions object maps emoji→[uid,...] — populated only if reactions exist
