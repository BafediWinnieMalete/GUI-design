# GUI2_dashboard.py - Dashboard with navigation
from PyQt5 import QtWidgets, QtGui, QtCore
import sys, os

class DashboardWindow(QtWidgets.QMainWindow):
    def __init__(self, username="User"):
        super().__init__()
        self.setWindowTitle("Dashboard - GUI 2")
        self.resize(600,400)
        self.username = username

        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        layout = QtWidgets.QVBoxLayout(central)

        # top: welcome + logo
        top_layout = QtWidgets.QHBoxLayout()
        self.label_welcome = QtWidgets.QLabel(f"Welcome, {{self.username}}")
        font = self.label_welcome.font()
        font.setPointSize(14)
        self.label_welcome.setFont(font)
        top_layout.addWidget(self.label_welcome)

        # optional logo if logo.png exists
        logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
        if os.path.exists(logo_path):
            pix = QtGui.QPixmap(logo_path).scaled(80,80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            lbl = QtWidgets.QLabel()
            lbl.setPixmap(pix)
            top_layout.addWidget(lbl)

        layout.addLayout(top_layout)

        # buttons to open calendar and library
        btn_layout = QtWidgets.QHBoxLayout()
        self.btn_calendar = QtWidgets.QPushButton("Open Calendar (GUI3)")
        self.btn_library = QtWidgets.QPushButton("Open Library (GUI4)")
        self.btn_logout = QtWidgets.QPushButton("Logout")
        btn_layout.addWidget(self.btn_calendar)
        btn_layout.addWidget(self.btn_library)
        btn_layout.addWidget(self.btn_logout)
        layout.addLayout(btn_layout)

        # small instruction label
        self.label_info = QtWidgets.QLabel("Use the buttons above to navigate to other GUIs.")
        layout.addWidget(self.label_info)

        # connections
        self.btn_calendar.clicked.connect(self.open_calendar)
        self.btn_library.clicked.connect(self.open_library)
        self.btn_logout.clicked.connect(self.logout)

    def open_calendar(self):
        try:
            from GUI3_calendar import CalendarWindow
            self.cal = CalendarWindow(parent=self)
            self.cal.show()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Could not open calendar:\n{e}")

    def open_library(self):
        try:
            from GUI4_library import LibraryWindow
            self.lib = LibraryWindow(parent=self)
            self.lib.show()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Could not open library:\n{e}")

    def logout(self):
        # close dashboard and return to login (simple behaviour: close window)
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = DashboardWindow("Malete")
    win.show()
    sys.exit(app.exec_())
