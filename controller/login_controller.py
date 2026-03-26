from PySide6.QtWidgets import QMessageBox

from view.login_view import LoginView

class LoginController:
    def __init__(self):
        self.view = LoginView()

    def show(self):
        self.view.show()