
import pytest
import task_manager
import database


@pytest.fixture
def test_db(tmp_path, monkeypatch):
    db_path = tmp_path / "test_tasks.db"
    monkeypatch.setattr(database, "DB_NAME", str(db_path))
    database.create_table()


def test_add_task(test_db):
    task_manager.add_task("Study for Exam", "2026-10-30")
    tasks = task_manager.view_tasks()

    assert len(tasks) == 1
    assert tasks[0][1] == "Study for Exam"


def test_empty_task_name(test_db):
    with pytest.raises(ValueError):
        task_manager.add_task("", "2026-10-30")


def test_complete_task(test_db):
    task_manager.add_task("Finish Assignment", "2026-10-30")
    task_id = task_manager.view_tasks()[0][0]

    task_manager.complete_task(task_id)

    assert task_manager.view_tasks()[0][3] == 1


def test_delete_task(test_db):
    task_manager.add_task("Read Chapter", "2026-10-30")
    task_id = task_manager.view_tasks()[0][0]

    task_manager.delete_task(task_id)

    assert task_manager.view_tasks() == []

