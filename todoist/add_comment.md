# <arg>=required  →=returns  !=errors
python add_comment.py <task_id> <content>
task_id:str  Todoist task id
content:str  Comment text (markdown supported)
→ {id content posted_at task_id}
# To reply to a comment, use get_comments to read thread then add_comment with context
# Reactions (likes) are not exposed in the REST API v1
! HTTP 404 if task not found
