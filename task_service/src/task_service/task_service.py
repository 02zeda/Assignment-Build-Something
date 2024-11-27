from fastapi import FastAPI , HTTPException, Request
from pydantic import BaseModel
import psycopg2
import time
class Task(BaseModel):
    title: str
    user_id: int
timeout = 5
start_time = time.time()
passed_time = 0
is_connected = False
def setup(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, title TEXT, user_id INT)")
    connection.commit()
    cursor.close()
while not is_connected:
    try:
        connection = psycopg2.connect(
            database="task_service_db",
            host = "postgres",
            user = "postgres",
            password = "password",
            port = "5432")
        print("Connected to the database")
        setup(connection)
        is_connected = True
    except:
        time.sleep(2)
        passed_time += time.time() -start_time
        print(f"Connection failed. Retrying in 2 seconds. Time passed: {passed_time}")
        continue



def create_task(title:str, user_id:int,connection):
    try:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO tasks (title, user_id) VALUES ('{title}', {user_id})")
        connection.commit()
        cursor.close()
    except:
        cursor.close()
        return False
    return True
def delete_task(task_id:int,connection):
    cursor = connection.cursor()
    try:
        cursor.execute(f"DELETE FROM tasks WHERE id = {task_id}")
        connection.commit()
    except:
        cursor.close()
        return False
    cursor.close()
    return True
def delete_all_tasks(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE * FROM tasks")
    connection.commit()
    cursor.close()
def get_tasks(user_id:int,connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id,))
        tasks = cursor.fetchall()
        cursor.close()
        tasks = [{"id": task[0], "title": task[1]} for task in tasks]
        #tasks.append({"id": 1, "title": "Task 1"})

        return tasks
    except:
        cursor.close()
        raise HTTPException(status_code=404, detail="User not found")

app = FastAPI()
@app.get("/tasks/{user_id:int}")
async def get_user_tasks(user_id:int):
    tasks =get_tasks(user_id,connection)
    print("Getting tasks, Good luck!")
    return tasks
@app.post("/tasks/")
async def create_user_task(task:Task):
    if create_task(task.title,task.user_id,connection):
        return {"message": "Task created"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
@app.delete("/tasks/{task_id}")
async def delete_user_task(task_id:int):
    if delete_task(task_id,connection):
        return {"message": "Task deleted"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")




