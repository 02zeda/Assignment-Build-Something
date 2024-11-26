"test_app.py"
from streamlit.testing.v1 import AppTest
import time
from unittest.mock import patch
def login(app_test:AppTest):
    app_test.sidebar.selectbox(key="login_register").select("Login").run()
    app_test.sidebar.text_input(key="username_input").input("test_user").run()
    app_test.sidebar.text_input(key="password_input").input("test_password").run()
    app_test.sidebar.button(key="login_button").click().run()
def logout(app_test:AppTest):
    login(app_test)
    timeout = 1
    time.sleep(timeout)
    app_test.sidebar.button(key="logout_button").click().run()
def test_login_labels():
    "A user opens the app and sees the login form."
    app_test = AppTest.from_file("frontend/src/app.py").run()
    assert app_test.sidebar.selectbox(key="login_register").label == "Choose Action"
    app_test.sidebar.selectbox(key="login_register").select("Login").run()
    assert app_test.sidebar.text_input(key="username_input").label == "Username"
    assert app_test.sidebar.text_input(key="password_input").label == "Password"


def test_login():
    "A user writes their username and password and clicks the login button. They then logout."

    app_test =AppTest.from_file("frontend/src/app.py").run()

    login(app_test)
    assert app_test.sidebar.button(key="login_button").value == True
    assert app_test.session_state.token != None
# def test_logout():
#     "A user logs in, then logs out."
#     with patch("streamlit.runtime.state.session_state.SessionState", autospec=True) as mock_state:
#         mock_state.return_value = {
#             "username_input": "test_user",
#             "password_input": "test_password",
#             "token": "mock_token",
#             "login_register": "Login"
#         }
#     app_test = AppTest.from_file("frontend/app.py").run()
#     app_test.session_state["token"] = "mock_token"
#     try:
#         app_test.sidebar.button(key="logout_button").click().run()
#     except KeyError:
#         raise AssertionError("Logout button was not rendered correctly.")
#     assert app_test.session_state.token == None

def test_register():
    pass
