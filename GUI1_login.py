# GUI1_login.py - Login screen
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import os

# hardcoded credentials (as requested)
USERNAME = "Malete"
PASSWORD = "68157304"

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login - GUI 1")
        self.resize(400,200)

        # layout
        layout = QtWidgets.QVBoxLayout()

        form = QtWidgets.QFormLayout()
        self.input_user = QtWidgets.QLineEdit()
        self.input_pass = QtWidgets.QLineEdit()
        self.input_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        form.addRow("Username:", self.input_user)
        form.addRow("Password:", self.input_pass)
        layout.addLayout(form)

        btn_layout = QtWidgets.QHBoxLayout()
        self.btn_login = QtWidgets.QPushButton("Login")
        self.btn_cancel = QtWidgets.QPushButton("Cancel")
        btn_layout.addWidget(self.btn_login)
        btn_layout.addWidget(self.btn_cancel)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        self.btn_login.clicked.connect(self.try_login)
        self.btn_cancel.clicked.connect(self.close)

    def try_login(self):
        user = self.input_user.text().strip()
        pwd = self.input_pass.text().strip()
        if user.lower() == USERNAME.lower() and pwd == PASSWORD:
            QMessageBox.information(self, "Success", "Login successful. Opening Dashboard...")
            # open dashboard (GUI2)
            try:
                from GUI2_dashboard import DashboardWindow
                self.dashboard = DashboardWindow(user)
                self.dashboard.show()
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open dashboard:\n{e}")
        else:
            QMessageBox.warning(self, "Login failed", "Incorrect username or password.\nUse your own surname and student number.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = LoginWindow()
    w.show()
    sys.exit(app.exec_())
