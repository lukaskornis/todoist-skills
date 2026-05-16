# <arg>=required  [arg]=optional  →=returns  #=note

- get_tasks:    list active tasks; filter by project, Todoist filter string, or limit
- create_task:  create a task with title, priority, due date, description, labels, or parent
- close_task:   mark a task complete by id
- update_task:  patch one or more fields on an existing task (content, priority, due, etc.)
- get_projects: list all projects — use returned ids as --project arg in get_tasks/create_task
