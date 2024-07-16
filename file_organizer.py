from PyQt5.QtWidgets import QMainWindow, QPushButton, QFileDialog, QMessageBox, QVBoxLayout, QWidget
from file_utils import get_folder_for_file, move_file_to_folder, is_file_valid
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
        files, _ = QFileDialog.getOpenFileNames(self, "Load your files", "", "All Files (*);;", options=options)
        for file_path in files:
            if file_path:
                folder_name = get_folder_for_file(file_path)
                if folder_name:
                    if is_file_valid(file_path):
                        if move_file_to_folder(file_path, folder_name):
                            QMessageBox.information(self, 'File Moved', f'File moved to {folder_name} folder')
                        else:
                            QMessageBox.warning(self, 'File Exists', f'A file with the same name as {file_path} already exists and was not replaced.')
                    else:
                        QMessageBox.warning(self, 'File Damaged', f'The file {file_path} is damaged and cannot be moved.')
                else:
                    QMessageBox.warning(self, 'File Not Supported', f'Sorry, the file type of {file_path} is not supported.')
