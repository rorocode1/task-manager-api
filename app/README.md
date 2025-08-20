# Task Manager API

A simple REST API for managing tasks using FastAPI.

## Features
- Create, read, update, delete tasks
- Auto-assign task IDs
- Optional priority and due date fields
- Fully documented Swagger UI

## Run Locally
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the API: `uvicorn app.main:app --reload`
4. Open browser: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Example Task JSON
```json
{
  "title": "Finish homework",
  "description": "Complete Python project",
  "completed": false,
  "priority": "high",
  "due_date": "2025-08-25"
}
