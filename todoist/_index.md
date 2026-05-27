# <arg>=required  [arg]=optional  →=returns  #=note

## Tasks
- get_tasks:          list active tasks; filter by project, Todoist filter string, or limit
- get_section_tasks:  list active tasks in a specific section by section_id
- create_task:    create a task; use --parent to make it a subtask immediately
- close_task:     mark a task complete by id
- update_task:    patch content, priority, due, description, or labels on an existing task
- move_task:      move a task to a section, project, or make it a subtask (--parent)

## Comments
- get_comments:   list all comments on a task (includes reactions map)
- add_comment:    post a comment on a task (markdown supported; no threading in Todoist)

## Projects & sections
- get_projects:    list all projects — ids used by get_tasks / create_task / move_task
- browse_project:  full project view: sections + tasks grouped (one call)
- create_project:  create a project with optional color, parent, or favorite flag
- get_sections:    list sections in a project — ids used by move_task / create_task
- create_section:  create a new section inside a project

## Notes
- Subtasks: use create_task --parent <id>  or  move_task --parent <id>
- Reactions/likes on comments: not exposed in REST API v1 (field exists, endpoint returns 404)
