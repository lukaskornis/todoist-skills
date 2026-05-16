# Todoist Skills

Token-efficient CLI wrappers for the Todoist REST API — one Python script per operation.

## Setup

Put your API token in `config.json`:
```json
{ "todoist_token": "<your_token>" }
```
Get your token at https://app.todoist.com/app/settings/integrations/developer

No dependencies beyond the Python standard library.

## Usage

```
python todoist/<skill>.py [args]
```

All scripts print JSON to stdout. Errors are prefixed with `ERROR:` and exit with code 1.

## Available skills

See [`todoist/_index.md`](./todoist/_index.md) for the full list and signatures.
Each skill has a matching `.md` file with argument docs and return shape.

## Quick reference

```bash
# List / browse projects
python todoist/get_projects.py                                 # list all
python todoist/browse_project.py <project_id>                 # full view: sections + tasks
python todoist/create_project.py "My Project" --color red     # new project
python todoist/create_project.py "Sub" --parent <project_id> --favorite

# List tasks
python todoist/get_tasks.py --filter "today"
python todoist/get_tasks.py --filter "p4 & overdue"
python todoist/get_tasks.py --project <project_id> --limit 10

# Create tasks
python todoist/create_task.py "Buy milk" --priority 2 --due "tomorrow"
python todoist/create_task.py "Sub-task" --parent <task_id>   # creates subtask

# Update / complete
python todoist/update_task.py <task_id> --priority 4 --due "today"
python todoist/close_task.py <task_id>

# Move tasks between sections / projects
python todoist/get_projects.py                                 # find project ids
python todoist/get_sections.py <project_id>                   # find section ids
python todoist/create_section.py <project_id> "Sprint 2"      # new section
python todoist/move_task.py <task_id> --section <section_id>  # move to section
python todoist/move_task.py <task_id> --project <project_id>  # move to project root
python todoist/move_task.py <task_id> --parent <task_id>      # nest as subtask

# Comments
python todoist/get_comments.py <task_id>
python todoist/add_comment.py <task_id> "Looks good, shipping tomorrow"
```
