import os
import shutil
from PyQt5.QtWidgets import QLabel, QMessageBox
from PyQt5.QtCore import Qt

class FileDropLabel(QLabel):
    def __init__(self, parent=None):
        super(FileDropLabel, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setText('Drag your file to this field:')
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("QLabel { border: 2px dashed #aaa; font-size: 24px; }")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if self.is_image(file_path):
                    self.move_to_images_folder(file_path)
                    QMessageBox.information(self, 'File Detected', f'File moved sucesfully')
                else:
                    QMessageBox.warning(self, 'File Not Supported', 'Sorry we cannot help you with that type of file')
                break

    def is_image(self, file_path):
        return file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))

    def move_to_images_folder(self, file_path):
        images_folder = os.path.join(os.getcwd(), 'images')
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
        shutil.move(file_path, images_folder)
