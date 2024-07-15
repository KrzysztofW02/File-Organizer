import os
import shutil
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox, QVBoxLayout, QWidget
from file_drop import FileDropLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Organizer")
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
        file_path, _ = QFileDialog.getOpenFileName(self, "Load your file", "", "All Files (*);;Image Files (*.png *.jpg *.jpeg *.gif *.bmp)", options=options)
        if file_path:
            if self.is_image(file_path):
                self.move_to_images_folder(file_path)
                QMessageBox.information(self, 'File Detected', f'File moved sucesfully')
            else:
                QMessageBox.warning(self, 'File Not Supported', 'Sorry we cannot help you with that type of file')

    def is_image(self, file_path):
        return file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))

    def move_to_images_folder(self, file_path):
        images_folder = os.path.join(os.getcwd(), 'images')
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
        shutil.move(file_path, images_folder)
