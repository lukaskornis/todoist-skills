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
# List all tasks
python todoist/get_tasks.py

# Filter tasks (Todoist filter syntax)
python todoist/get_tasks.py --filter "today"
python todoist/get_tasks.py --filter "p4 & overdue"
python todoist/get_tasks.py --project <project_id> --limit 10

# Create a task
python todoist/create_task.py "Buy milk" --priority 2 --due "tomorrow"
python todoist/create_task.py "Sub-task" --parent <task_id>

# Update a task
python todoist/update_task.py <task_id> --priority 4 --due "today"

# Complete a task
python todoist/close_task.py <task_id>

# List projects (to get project ids)
python todoist/get_projects.py
```
