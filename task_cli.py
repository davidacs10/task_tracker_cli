import sys


if len(sys.argv) < 2:
    print(f"Uso: python task_cli.py <command>")
    sys.exit(1)
else:
    command = sys.argv[1]
    print(f"Comando recibido: <{command}>")
