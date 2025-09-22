# GUI4_library.py - Simple library (text file storage)
from PyQt5 import QtWidgets
import sys, os

BOOKS_FILE = "books.txt"

class LibraryWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Library - GUI 4")
        self.resize(600,400)
        layout = QtWidgets.QVBoxLayout(self)

        form = QtWidgets.QFormLayout()
        self.input_title = QtWidgets.QLineEdit()
        self.input_author = QtWidgets.QLineEdit()
        form.addRow("Title:", self.input_title)
        form.addRow("Author:", self.input_author)
        layout.addLayout(form)

        btn_layout = QtWidgets.QHBoxLayout()
        self.btn_add = QtWidgets.QPushButton("Add Book (Save)")
        self.btn_load = QtWidgets.QPushButton("Load Books")
        self.btn_back = QtWidgets.QPushButton("Back to Dashboard")
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_load)
        btn_layout.addWidget(self.btn_back)
        layout.addLayout(btn_layout)

        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Title", "Author"])
        layout.addWidget(self.table)

        self.status = QtWidgets.QLabel("Status: ready")
        layout.addWidget(self.status)

        # connect
        self.btn_add.clicked.connect(self.add_book)
        self.btn_load.clicked.connect(self.load_books)
        self.btn_back.clicked.connect(self.close)

        # ensure file exists
        if not os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "w", encoding="utf-8") as f:
                f.write("")

    def add_book(self):
        title = self.input_title.text().strip()
        author = self.input_author.text().strip()
        if not title:
            self.status.setText("Status: Title required")
            return
        # append to text file
        try:
            with open(BOOKS_FILE, "a", encoding="utf-8") as f:
                f.write(f"{title}||{author}\n")
            self.status.setText("Status: Book saved to file")
            self.input_title.clear(); self.input_author.clear()
        except Exception as e:
            self.status.setText("Status: Error saving book: " + str(e))

    def load_books(self):
        self.table.setRowCount(0)
        try:
            with open(BOOKS_FILE, "r", encoding="utf-8") as f:
                lines = [l.strip() for l in f.readlines() if l.strip()]
            for i,ln in enumerate(lines):
                parts = ln.split('||')
                title = parts[0] if len(parts)>0 else ''
                author = parts[1] if len(parts)>1 else ''
                self.table.insertRow(i)
                self.table.setItem(i,0, QtWidgets.QTableWidgetItem(title))
                self.table.setItem(i,1, QtWidgets.QTableWidgetItem(author))
            self.status.setText(f"Status: Loaded {len(lines)} books")
        except Exception as e:
            self.status.setText("Status: Error loading books: " + str(e))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = LibraryWindow()
    w.show()
    sys.exit(app.exec_())
