from fastapi import FastAPI , HTTPException
from schemas import UserCreate, UserLogin
from auth import *
import psycopg2
import time

app = FastAPI()
imeout = 5
start_time = time.time()
passed_time = 0
is_connected = False
def setup(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id SERIAL , username TEXT PRIMARY KEY, password TEXT)")
    connection.commit()
    cursor.close()
while not is_connected:
    try:
        connection = psycopg2.connect(
            database="user_service_db",
            host = "postgres",
            user = "postgres",
            password = "password",
            port = "5432")
        print("Connected to the database")
        is_connected = True
        setup(connection)
    except:
        time.sleep(2)
        passed_time += time.time() -start_time
        print(f"Connection failed. Retrying in 2 seconds. Time passed: {passed_time}")
        continue

@app.post("/register/")
def register_user(user: UserCreate):
    cursor = connection.cursor()

    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{user.username}', '{hash_password(user.password)}')")
    connection.commit()



    cursor.close()
    return { "username": user.username}
@app.post("/login/")
async def login_user(user: UserLogin):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{user.username}'")
    result = cursor.fetchone()
    cursor.close()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(user.password, result[2]):
        raise HTTPException(status_code=403, detail="Invalid password")
    return { "token":result[0],"user": result[1]}

