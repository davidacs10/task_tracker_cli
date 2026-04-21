import sys
import json
import os
from datetime import datetime


def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            content = json.load(f)
            return content
    return []


def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(description):
    tasks = load_tasks()
    if tasks:
        ids = []
        for task in tasks:
            ids.append(task["id"])
        new_id = max(ids) + 1
    else:
        new_id = 1

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarea agregada exitosamente (ID: {new_id})")


if len(sys.argv) < 2:
    print(f"Uso: python task_cli.py <command>")
    sys.exit(1)
else:
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Por favor, agregue una descripcion.")
        else:
            add_task(sys.argv[2])
