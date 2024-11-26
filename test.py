import requests
TASK_SERVICE_URL = "http://localhost:8000"
def get_tasks(token=1):
    response = requests.get(f"{TASK_SERVICE_URL}/tasks/{token}")
    return response.json()
def create_task(token =1, title = "Task 1"):
    response = requests.post(f"{TASK_SERVICE_URL}/tasks", json={"title": title, "user_id": token})
    return response.json()
def delete_task(token = 1, task_id = 1):
    response = requests.delete(f"{TASK_SERVICE_URL}/tasks/{task_id}")
    return response.json()
#print(create_task())
print(get_tasks())
print(create_task())
print(delete_task())