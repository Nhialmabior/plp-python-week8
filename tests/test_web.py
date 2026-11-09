
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import web.database as database


class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.temp_directory = tempfile.TemporaryDirectory()

        test_directory = Path(cls.temp_directory.name)

        cls.database_patcher = patch.object(
            database, "DATABASE", test_directory / "test_tasks.db"
        )
        cls.instance_patcher = patch.object(
            database, "INSTANCE_DIR", test_directory
        )

        cls.database_patcher.start()
        cls.instance_patcher.start()

        from web.app import app

        cls.app = app
        cls.app.config["TESTING"] = True
        cls.client = cls.app.test_client()

        database.initialize_database()

    @classmethod
    def tearDownClass(cls):
        cls.database_patcher.stop()
        cls.instance_patcher.stop()
        cls.temp_directory.cleanup()

    def setUp(self):
        with database.get_connection() as connection:
            connection.execute("DELETE FROM tasks")

    def test_homepage_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_tasks(self):
        response = self.client.get("/api/tasks")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_add_task(self):
        response = self.client.post(
            "/api/tasks",
            json={"title": "Learn Flask"}
        )

        self.assertEqual(response.status_code, 201)

        tasks = self.client.get("/api/tasks").json

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Learn Flask")

    def test_reject_empty_task(self):
        response = self.client.post(
            "/api/tasks",
            json={"title": ""}
        )

        self.assertEqual(response.status_code, 400)

    def test_complete_task(self):
        task = self.client.post(
            "/api/tasks",
            json={"title": "Test completion"}
        ).json

        response = self.client.patch(
            f"/api/tasks/{task['id']}",
            json={"completed": True}
        )

        self.assertEqual(response.status_code, 200)

        tasks = self.client.get("/api/tasks").json

        self.assertEqual(tasks[0]["completed"], 1)

    def test_delete_task(self):
        task = self.client.post(
            "/api/tasks",
            json={"title": "Delete me"}
        ).json

        response = self.client.delete(
            f"/api/tasks/{task['id']}"
        )

        self.assertEqual(response.status_code, 200)

        tasks = self.client.get("/api/tasks").json

        self.assertEqual(tasks, [])


if __name__ == "__main__":
    unittest.main()
