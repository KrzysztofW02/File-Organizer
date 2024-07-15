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
                QMessageBox.information(self, 'File Detected', f'File detected: {file_path}')
                break