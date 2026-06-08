from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):

    if not validate_task_title(title):
        return

    if not validate_task_description(description):
        return

    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully")


def mark_task_as_complete(tasks, title):

    for task in tasks:
        if task["title"] == title:
            task["completed"] = True
            print("Task marked as complete")
            return

    print("Task not found")


def view_pending_tasks(tasks):

    found = False

    for task in tasks:
        if not task["completed"]:
            print(
                f"{task['title']} - "
                f"{task['description']} - "
                f"Due: {task['due_date']}"
            )
            found = True

    if not found:
        print("No pending tasks")


def calculate_progress(tasks):

    if len(tasks) == 0:
        print("No tasks available")
        return

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    progress = (completed / len(tasks)) * 100

    print(f"Progress: {progress:.2f}%")