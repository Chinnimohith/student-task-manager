
from database import get_connection


def add_task(task_name, due_date):
    if not task_name.strip():
        raise ValueError("Task name cannot be empty")

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO tasks (task_name, due_date) VALUES (?, ?)",
            (task_name.strip(), str(due_date))
        )


def view_tasks():
    with get_connection() as conn:
        return conn.execute(
            "SELECT * FROM tasks ORDER BY id"
        ).fetchall()


def complete_task(task_id):
    with get_connection() as conn:
        conn.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?",
            (task_id,)
        )


def delete_task(task_id):
    with get_connection() as conn:
        conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
