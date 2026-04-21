import sys
import json
import os
from datetime import datetime


def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            try:
                content = json.load(f)
                return content
            except json.JSONDecodeError:
                print("Error: task.json esta corrupto.")
                sys.exit(1)
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


def delete_task(id: int):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            found = True
            break
    if not found:
        print("Tarea no encontrada.")
    else:
        save_tasks(tasks)
        print("Tarea eliminada con exito.")


def update_task(id: int, description):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == id:
            task["description"] = description
            task["updatedAt"] = now
            found = True
            break
    if not found:
        print("Tarea no encontrada.")
    else:
        save_tasks(tasks)
        print("Tarea actualizada con exito.")


def mark_task(id, status):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == id:
            task["status"] = status
            task["updatedAt"] = now
            found = True
            break
    if not found:
        print("Tarea no encontrada.")
    else:
        save_tasks(tasks)
        print(f"Tarea marcada como {status} con exito.")


def list_tasks(status=None):
    tasks = load_tasks()
    if not tasks:
        print("No hay tareas.")
        return

    for task in tasks:
        if status is None or task["status"] == status:
            print(f"[{task['id']}] {task['description']} ({task['status']})")


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
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Por favor, escriba un ID valido.")
        else:
            try:
                delete_task(int(sys.argv[2]))
            except ValueError:
                print("El ID debe ser un numero entero.")
    elif command == "update":
        if len(sys.argv) < 3:
            print("Por favor, escriba un ID valido.")
        elif len(sys.argv) < 4:
            print("Por favor, agregue una descripcion.")
        else:
            try:
                update_task(int(sys.argv[2]), sys.argv[3])
            except ValueError:
                print("El ID debe ser un numero entero.")
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Por favor, escriba un ID valido.")
        else:
            try:
                mark_task(int(sys.argv[2]), "in-progress")
            except ValueError:
                print("El ID debe ser un numero entero.")
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Por favor, escriba un ID valido.")
        else:
            try:
                mark_task(int(sys.argv[2]), "done")
            except ValueError:
                print("El ID debe ser un numero entero.")
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    else:
        print("Comando no reconocido.")
