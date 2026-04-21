# Task Tracker CLI

Gestor de tareas por línea de comandos construido en Python. Permite agregar, actualizar, eliminar y listar tareas, guardándolas en un archivo JSON.

## Requisitos

- Python 3.x

## Uso

### Agregar una tarea

```bash
python task_cli.py add "Descripcion de la tarea"
```

### Actualizar una tarea

```bash
python task_cli.py update <id> "Nueva descripcion"
```

### Eliminar una tarea

```bash
python task_cli.py delete <id>
```

### Marcar una tarea como en progreso

```bash
python task_cli.py mark-in-progress <id>
```

### Marcar una tarea como completada

```bash
python task_cli.py mark-done <id>
```

### Listar tareas

```bash
# Todas las tareas
python task_cli.py list

# Solo tareas pendientes
python task_cli.py list todo

# Solo tareas en progreso
python task_cli.py list in-progress

# Solo tareas completadas
python task_cli.py list done
```

## Estados de una tarea

| Estado        | Descripcion                      |
| ------------- | -------------------------------- |
| `todo`        | Tarea pendiente (estado inicial) |
| `in-progress` | Tarea en progreso                |
| `done`        | Tarea completada                 |

## Estructura del JSON

Las tareas se guardan automaticamente en un archivo `tasks.json` con la siguiente estructura:

```json
[
  {
    "id": 1,
    "description": "Comprar leche",
    "status": "todo",
    "createdAt": "2026-04-20 10:00:00",
    "updatedAt": "2026-04-20 10:00:00"
  }
]
```

## Proyecto basado en

[roadmap.sh - Task Tracker](https://roadmap.sh/projects/task-tracker)
