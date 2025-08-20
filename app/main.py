from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Task Manager API")

tasks = []

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    priority: Optional[str] = "medium"  # low, medium, high
    due_date: Optional[str] = None       # YYYY-MM-DD

# Get all tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Create a new task with auto-assigned ID
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    if tasks:
        next_id = max(t.id for t in tasks) + 1
    else:
        next_id = 1
    task.id = next_id
    tasks.append(task)
    return task

# Get a single task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Update a task by ID
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            updated_task.id = task_id  # Ensure ID stays the same
            tasks[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Delete a task by ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return {"detail": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
