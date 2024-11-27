import pytest
import psycopg2
from task_service.src.task_service.task_service import setup, create_task, delete_task, get_tasks,delete_all_tasks

@pytest.fixture(scope="module")
def connection():
    connection = psycopg2.connect(
    database="task_service_db",
    host = "localhost",
    user = "postgres",
    password = "password",
    port = "5432")
    setup(connection)
    yield connection
def test_connection():
    connection = psycopg2.connect(
    database="task_service_db",
    host = "localhost",
    user = "postgres",
    password = "password",
    port = "5432")
    cursor = connection.cursor()
    assert cursor.closed == 0
    assert connection.closed == 0




