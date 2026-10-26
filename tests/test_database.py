
import pytest
import database
from task_manager import add_task, view_tasks, complete_task, delete_task


@pytest.fixture
def test_db(tmp_path, monkeypatch):
    db_path = tmp_path / "integration_tasks.db"
    monkeypatch.setattr(database, "DB_NAME", str(db_path))
    database.create_table()


def test_database_storage(test_db):
    add_task("Database Test", "2026-11-01")

    tasks = view_tasks()

    assert len(tasks) == 1
    assert tasks[0][1] == "Database Test"
    assert tasks[0][2] == "2026-11-01"
    assert tasks[0][3] == 0


def test_complete_workflow(test_db):
    add_task("Finish Project", "2026-11-05")

    task_id = view_tasks()[0][0]

    complete_task(task_id)
    assert view_tasks()[0][3] == 1

    delete_task(task_id)
    assert view_tasks() == []
