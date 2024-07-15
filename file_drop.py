from PyQt5.QtWidgets import QLabel, QMessageBox
from PyQt5.QtCore import Qt
from file_utils import get_folder_for_file, move_file_to_folder, is_file_valid

class FileDropLabel(QLabel):
    def __init__(self, parent=None):
        super(FileDropLabel, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setText('Drag your files to this field:')
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("QLabel { border: 2px dashed #aaa; font-size: 24px; }")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                folder_name = get_folder_for_file(file_path)
                if folder_name:
                    if is_file_valid(file_path):
                        if move_file_to_folder(file_path, folder_name):
                            QMessageBox.information(self, 'File Moved', f'File {file_path} moved to {folder_name} folder')
                        else:
                            QMessageBox.warning(self, 'File Exists', f'A file with the name {file_path} already exists and was not replaced.')
                    else:
                        QMessageBox.warning(self, 'File Damaged', f'The file {file_path} is damaged and cannot be moved.')
                else:
                    QMessageBox.warning(self, 'File Not Supported', f'Sorry, the file type of {file_path} is not supported.')
