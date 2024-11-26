import streamlit as st
import requests
import time
# Base URLs for the microservices
USER_SERVICE_URL = "http://localhost:8000"
TASK_SERVICE_URL = "http://<task-service-url>"
# Initialize session state variables
if "username_input" not in st.session_state:
    st.session_state["username_input"] = ""
if "password_input" not in st.session_state:
    st.session_state["password_input"] = ""
if "token" not in st.session_state:
    st.session_state["token"] = None
if "login_register" not in st.session_state:
    st.session_state["login_register"] = "Login"

# Helper functions for API calls
def register_user(username, password):
    # response = requests.post(f"{USER_SERVICE_URL}/register/", json={"username": username, "password": password})
    # return response.json()
    return {"username": username}

def login_user(username, password):
    #response = requests.post(f"{USER_SERVICE_URL}/login/", json={"username": username, "password": password})
    #return response.json()
    return  {"token": "123456"}

def get_tasks(token):
    token = 1
    #headers = {"Authorization": f"Token {token}"}

    #response = requests.get(f"{TASK_SERVICE_URL}/tasks/", headers=headers)
    response = requests.get(f"{TASK_SERVICE_URL}/tasks/{token}")
    return response.json()

def create_task(token, title):
    headers = {"Authorization": f"Token {token}"}
    #response = requests.post(f"{TASK_SERVICE_URL}/tasks/", headers=headers, json={"title": title})
    #return response.json()
    return 200

def delete_task(token, task_id):
    # headers = {"Authorization": f"Token {token}"}
    # response = requests.delete(f"{TASK_SERVICE_URL}/tasks/{task_id}/", headers=headers)
    # return response.status_code
    return 200
def show_tasks(tasks):
    for task in tasks:
        st.write(f"- {task['title']}")
# Streamlit app
st.title("Task Manager")

# User Authentication
if "token" not in st.session_state:
    st.session_state.token = None

if st.session_state.token is None:
    st.sidebar.title("Login / Register")
    option = st.sidebar.selectbox("Choose Action", ["Login", "Register"],key="login_register")

    if option == "Login":
        username = st.sidebar.text_input("Username",key="username_input")
        password = st.sidebar.text_input("Password", type="password",key="password_input")
        if st.sidebar.button("Login",key="login_button"):
            response = login_user(username, password)
            if "token" in response:
                st.session_state.token = response["token"]
                st.success("Login successful!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid credentials")
                time.sleep(1)
                st.rerun()


    elif option == "Register":
        username = st.sidebar.text_input("Username",key="register_username_input")
        password = st.sidebar.text_input("Password", type="password",key="register_password_input")
        if st.sidebar.button("Register",key="register_button"):
            response = register_user(username, password)
            if "username" in response:
                st.success("Registration successful! Please log in.")
            else:
                st.error("Registration failed")

else:
    st.sidebar.title("Logout")
    logout_button = st.sidebar.button("Logout",key="logout_button")
    if logout_button:
        st.session_state.token = None
        st.rerun()


    # Main app functionality
    st.subheader("Your Tasks")
    #tasks = get_tasks(st.session_state.token)
    tasks:dict = get_tasks(st.session_state.token)
    if not tasks:
        st.write("No tasks available.",key="no_tasks")
    else:
        for task in tasks:
            st.write(f"- {task['title']}")
            if st.button(f"Delete {task['title']}", key=task['id']):
                response_code = delete_task(st.session_state.token, task['id'])
                if response_code == 200:
                    success_task_message =st.success("Task deleted successfully!")
                    time.sleep(0.5)
                    success_task_message.empty()
                else:
                    task_failed_message = st.error("Task deletion failed")
                    time.sleep(0.5)
                    task_failed_message.empty()


    st.subheader("Add a Task")
    new_task = st.text_input("Task Title")

    if st.button("Add Task"):
        status_code =create_task(st.session_state.token, new_task)
        if status_code == 200:
            success_message = st.success("Task added successfully!")
            time.sleep(0.5)
            success_message.empty()
        else:
            error_message = st.error("Task addition failed")
            time.sleep(0.5)
            error_message.empty()
        st.rerun()
