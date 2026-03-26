import sys
from PySide6.QtWidgets import QApplication
from controller.login_controller import LoginController

def main():
    app = QApplication(sys.argv)

    controller = LoginController()
    controller.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()