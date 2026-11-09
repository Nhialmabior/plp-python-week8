
import sqlite3
from pathlib import Path
from contextlib import contextmanager

BASE_DIR = Path(__file__).resolve().parent.parent
INSTANCE_DIR = BASE_DIR / "instance"
DATABASE = INSTANCE_DIR / "tasks.db"


@contextmanager
def get_connection():
    INSTANCE_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def get_all_tasks():
    with get_connection() as connection:
        tasks = connection.execute("""
            SELECT id, title, completed, created_at
            FROM tasks
            ORDER BY id DESC
        """).fetchall()

    return [dict(task) for task in tasks]


def add_task(title):
    with get_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO tasks (title) VALUES (?)",
            (title,)
        )
        return cursor.lastrowid


def update_task(task_id, completed):
    with get_connection() as connection:
        cursor = connection.execute("""
            UPDATE tasks
            SET completed = ?
            WHERE id = ?
        """, (int(completed), task_id))

        return cursor.rowcount > 0


def delete_task(task_id):
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        return cursor.rowcount > 0
