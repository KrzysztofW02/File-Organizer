from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from file_drop import FileDropLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Organizezr")
        self.resize(700, 400)

        layout = QVBoxLayout()

        self.label = FileDropLabel()
        layout.addWidget(self.label)

        self.load_button = QPushButton("Load your file")
        self.load_button.setStyleSheet("font-size: 16px;")
        self.load_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.load_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Load your file", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_path:
            QMessageBox.information(self, 'File Detected', f'File detected: {file_path}')

