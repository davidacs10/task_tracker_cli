import unittest
from unittest.mock import patch
from task_cli import *


class TestAddTask(unittest.TestCase):
    @patch("task_cli.save_tasks")
    @patch("task_cli.load_tasks")
    def test_add_first_task(self, mock_load, mock_save):
        mock_load.return_value = []

        add_task("Comprar leche")

        saved_task = mock_save.call_args[0][0][0]

        self.assertEqual(saved_task["id"], 1)
        self.assertEqual(saved_task["description"], "Comprar leche")
        self.assertEqual(saved_task["status"], "todo")

    @patch("task_cli.save_tasks")
    @patch("task_cli.load_tasks")
    def test_add_second_task(self, mock_load, mock_save):
        mock_load.return_value = [
            {
                "id": 1,
                "description": "Tarea existente",
                "status": "todo",
                "createdAt": "2026-04-20 10:00:00",
                "updatedAt": "2026-04-20 10:00:00",
            }
        ]

        add_task("Estudiar")

        saved_task = mock_save.call_args[0][0][1]

        self.assertEqual(saved_task["id"], 2)
        self.assertEqual(saved_task["description"], "Estudiar")
        self.assertEqual(saved_task["status"], "todo")


class TestDeleteTask(unittest.TestCase):
    @patch("task_cli.save_tasks")
    @patch("task_cli.load_tasks")
    def test_delete_existent_task(self, mock_load, mock_save):
        mock_load.return_value = [
            {
                "id": 1,
                "description": "Tarea existente",
                "status": "todo",
                "createdAt": "2026-04-20 10:00:00",
                "updatedAt": "2026-04-20 10:00:00",
            }
        ]

        delete_task(1)

        saved_list = mock_save.call_args[0][0]
        self.assertEqual(saved_list, [])

    @patch("task_cli.save_tasks")
    @patch("task_cli.load_tasks")
    def test_delete_nonexistent_task(self, mock_load, mock_save):
        mock_load.return_value = []

        delete_task(99)

        mock_save.assert_not_called()


class TestUpdateTask(unittest.TestCase):
    @patch("task_cli.save_tasks")
    @patch("task_cli.load_tasks")
    def test_update_task(self, mock_load, mock_save):
        mock_load.return_value = [
            {
                "id": 1,
                "description": "Tarea existente",
                "status": "todo",
                "createdAt": "2026-04-20 10:00:00",
                "updatedAt": "2026-04-20 10:00:00",
            }
        ]

        update_task(1, "Ejercicio")

        saved_task = mock_save.call_args[0][0][0]
        self.assertEqual(saved_task["id"], 1)
        self.assertEqual(saved_task["description"], "Ejercicio")

    @patch("task_cli.save_tasks")
    @patch("task_cli.load_tasks")
    def test_update_nonexistent_task(self, mock_load, mock_save):
        mock_load.return_value = []

        update_task(99, "example")

        mock_save.assert_not_called()


class TestMarkTask(unittest.TestCase):
    @patch("task_cli.save_tasks")
    @patch("task_cli.load_tasks")
    def test_mark_task(self, mock_load, mock_save):
        mock_load.return_value = [
            {
                "id": 1,
                "description": "Tarea existente",
                "status": "todo",
                "createdAt": "2026-04-20 10:00:00",
                "updatedAt": "2026-04-20 10:00:00",
            }
        ]

        mark_task(1, "done")

        saved_task = mock_save.call_args[0][0][0]
        self.assertEqual(saved_task["id"], 1)
        self.assertEqual(saved_task["status"], "done")

    @patch("task_cli.save_tasks")
    @patch("task_cli.load_tasks")
    def test_mark_nonexistent_task(self, mock_load, mock_save):
        mock_load.return_value = [
            {
                "id": 1,
                "description": "Tarea existente",
                "status": "todo",
                "createdAt": "2026-04-20 10:00:00",
                "updatedAt": "2026-04-20 10:00:00",
            }
        ]

        mark_task(100, "in-progress")

        mock_save.assert_not_called()


if __name__ == "__main__":
    unittest.main()
