from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QCheckBox
)
from PySide6.QtCore import Qt

class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录")
        self.setFixedSize(350, 220)

        self.notice_label = QLabel("公告：请输入密钥登录系统")
        self.key_input = QLineEdit()
        self.remember_checkbox = QCheckBox("记住密钥")
        self.login_button = QPushButton("验证密钥")

        self.init_ui()

    def init_ui(self):

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 20, 30, 20)
        layout.setSpacing(16)

        # 公告文本
        notice_font = QFont()
        notice_font.setPointSize(12)

        self.notice_label.setFont(notice_font)
        self.notice_label.setWordWrap(True)
        self.notice_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.notice_label.setStyleSheet("color: rgb(178, 34, 34);")

        # 密钥输入框
        self.key_input.setPlaceholderText("请输入密钥")
        self.key_input.setEchoMode(QLineEdit.EchoMode.Normal)
        self.key_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.key_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # 记住密钥
        self.remember_checkbox.setStyleSheet("""
            QCheckBox::indicator {
                width: 14px;
                height: 14px;
            }
            QCheckBox {
                font-size: 12px;
            }
        """)

        # 登录按钮
        self.login_button.setFixedHeight(32)
        self.login_button.setFixedWidth(120)

        layout.addWidget(self.notice_label)
        layout.addWidget(self.key_input)
        layout.addWidget(self.remember_checkbox, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.login_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)