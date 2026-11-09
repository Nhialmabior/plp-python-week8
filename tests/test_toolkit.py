"""Unit tests for the Personal Mini-Toolkit."""

import unittest
from unittest.mock import patch

from toolkit import add_task, complete_task, remove_task, view_tasks


class ToDoListTests(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        with patch("builtins.input", return_value="Finish PLP assignment"):
            add_task(tasks)
        self.assertEqual(tasks, ["Finish PLP assignment"])

    def test_empty_task_is_not_added(self):
        tasks = []
        with patch("builtins.input", return_value="   "):
            add_task(tasks)
        self.assertEqual(tasks, [])

    def test_complete_task(self):
        tasks = ["Read Python notes"]
        with patch("builtins.input", return_value="1"):
            complete_task(tasks)
        self.assertEqual(tasks, ["Read Python notes [Completed]"])

    def test_task_cannot_be_completed_twice(self):
        tasks = ["Read Python notes [Completed]"]
        with patch("builtins.input", return_value="1"):
            complete_task(tasks)
        self.assertEqual(tasks, ["Read Python notes [Completed]"])

    def test_invalid_task_number_does_not_change_list(self):
        tasks = ["Task one"]
        with patch("builtins.input", return_value="9"):
            remove_task(tasks)
        self.assertEqual(tasks, ["Task one"])

    def test_non_numeric_task_number_does_not_change_list(self):
        tasks = ["Task one"]
        with patch("builtins.input", return_value="abc"):
            complete_task(tasks)
        self.assertEqual(tasks, ["Task one"])

    def test_remove_task(self):
        tasks = ["Task one", "Task two"]
        with patch("builtins.input", return_value="2"):
            remove_task(tasks)
        self.assertEqual(tasks, ["Task one"])

    def test_view_empty_list(self):
        with patch("builtins.print") as mocked_print:
            view_tasks([])
        self.assertTrue(
            any("to-do list is empty" in str(call).lower() for call in mocked_print.call_args_list)
        )


if __name__ == "__main__":
    unittest.main()
