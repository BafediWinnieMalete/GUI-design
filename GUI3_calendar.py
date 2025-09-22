# GUI3_calendar.py - Calendar widget
from PyQt5 import QtWidgets, QtCore
import sys

class CalendarWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calendar - GUI 3")
        self.resize(400,350)
        layout = QtWidgets.QVBoxLayout(self)
        self.calendar = QtWidgets.QCalendarWidget()
        layout.addWidget(self.calendar)

        btn_layout = QtWidgets.QHBoxLayout()
        self.btn_back = QtWidgets.QPushButton("Back to Dashboard")
        btn_layout.addWidget(self.btn_back)
        layout.addLayout(btn_layout)

        self.btn_back.clicked.connect(self.close)
        # show selected date in status label
        self.lbl_date = QtWidgets.QLabel("Selected date: -")
        layout.addWidget(self.lbl_date)
        self.calendar.selectionChanged.connect(self.update_label)

    def update_label(self):
        d = self.calendar.selectedDate()
        self.lbl_date.setText("Selected date: " + d.toString(QtCore.Qt.ISODate))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = CalendarWindow()
    w.show()
    sys.exit(app.exec_())
