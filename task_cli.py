import sys
import json
import os


if len(sys.argv) < 2:
    print(f"Uso: python task_cli.py <command>")
    sys.exit(1)
else:
    command = sys.argv[1]
    print(f"Comando recibido: <{command}>")


def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            content = json.load(f)
            return content
    return []


def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
