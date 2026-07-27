import json
import os
import sys
from datetime import datetime

FILE_NAME = "tasks.json"


# ----------------------------
# File Handling
# ----------------------------

def load_tasks():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ----------------------------
# Utility Functions
# ----------------------------

def next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


# ----------------------------
# Commands
# ----------------------------

def add_task(description):
    tasks = load_tasks()

    now = datetime.now().isoformat()

    task = {
        "id": next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {task['id']})")


def update_task(task_id, description):
    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    task["description"] = description
    task["updatedAt"] = datetime.now().isoformat()

    save_tasks(tasks)

    print("Task updated successfully.")


def delete_task(task_id):
    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    tasks.remove(task)
    save_tasks(tasks)

    print("Task deleted successfully.")


def mark_status(task_id, status):
    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    task["status"] = status
    task["updatedAt"] = datetime.now().isoformat()

    save_tasks(tasks)

    print(f"Task marked as {status}.")


def list_tasks(status=None):
    tasks = load_tasks()

    if status:
        tasks = [task for task in tasks if task["status"] == status]

    if not tasks:
        print("No tasks found.")
        return

    print("-" * 80)

    for task in tasks:
        print(f"ID          : {task['id']}")
        print(f"Description : {task['description']}")
        print(f"Status      : {task['status']}")
        print(f"Created At  : {task['createdAt']}")
        print(f"Updated At  : {task['updatedAt']}")
        print("-" * 80)


# ----------------------------
# CLI
# ----------------------------

def help_menu():
    print("""
Task Tracker CLI

Usage:

python task_cli.py add "Task description"

python task_cli.py update <id> "New description"

python task_cli.py delete <id>

python task_cli.py mark-in-progress <id>

python task_cli.py mark-done <id>

python task_cli.py list

python task_cli.py list done

python task_cli.py list todo

python task_cli.py list in-progress
""")


def main():
    args = sys.argv

    if len(args) < 2:
        help_menu()
        return

    command = args[1]

    try:

        if command == "add":
            add_task(args[2])

        elif command == "update":
            update_task(int(args[2]), args[3])

        elif command == "delete":
            delete_task(int(args[2]))

        elif command == "mark-in-progress":
            mark_status(int(args[2]), "in-progress")

        elif command == "mark-done":
            mark_status(int(args[2]), "done")

        elif command == "list":
            if len(args) == 2:
                list_tasks()
            else:
                list_tasks(args[2])

        else:
            help_menu()

    except IndexError:
        print("Invalid command. Check the required arguments.")

    except ValueError:
        print("Task ID must be an integer.")


if __name__ == "__main__":
    main()