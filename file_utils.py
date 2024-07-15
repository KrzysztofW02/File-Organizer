import os
import shutil
from PIL import Image
from PyPDF2 import PdfFileReader
from PyQt5.QtWidgets import QMessageBox
import mimetypes
import zipfile
import tarfile
import rarfile

FILE_TYPE_FOLDERS = {
    '.png': 'images',
    '.jpg': 'images',
    '.jpeg': 'images',
    '.gif': 'images',
    '.bmp': 'images',
    '.txt': 'texts',
    '.md': 'texts',
    '.log': 'texts',
    '.pdf': 'pdfs',
    '.doc': 'documents',
    '.docx': 'documents',
    '.odt': 'documents',
    '.ppt': 'presentations',
    '.pptx': 'presentations',
    '.mp3': 'audio',
    '.wav': 'audio',
    '.mp4': 'videos',
    '.avi': 'videos',
    '.mkv': 'videos',
    '.zip': 'archives',
    '.rar': 'archives',
    '.tar': 'archives',
    '.gz': 'archives',
    '.exe': 'executables',
    '.msi': 'executables',
    '.apk': 'executables',
    '.html': 'web',
    '.css': 'web',
    '.js': 'web',
    '.py': 'code',
    '.c': 'code',
    '.cpp': 'code',
    '.java': 'code',
    '.class': 'code',
    '.cs': 'code',
    '.vb': 'code',
    '.php': 'code',
    '.rb': 'code',
    '.go': 'code',
    '.xlsx': 'excel',
    '.csv': 'excel',
    '.xlsm': 'excel',
    '.ppt': 'presentations',
    '.pptx': 'presentations',
    '.pps': 'presentations',
    '.ppsx': 'presentations',
    '.odp': 'presentations',
}

def get_folder_for_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    return FILE_TYPE_FOLDERS.get(extension)

def is_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except (IOError, SyntaxError):
        return False

def is_text(file_path):
    try:
        with open(file_path, 'r') as file:
            file.read()
        return True
    except:
        return False

def is_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PdfFileReader(file)
            if reader.getNumPages() > 0:
                return True
        return False
    except:
        return False

def is_audio(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith('audio/')

def is_video(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith('video/')

def is_archive(file_path):
    try:
        if file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                if zip_ref.testzip() is None:
                    return True
        elif file_path.endswith('.tar') or file_path.endswith('.gz'):
            with tarfile.open(file_path, 'r') as tar_ref:
                tar_ref.getmembers()
            return True
        elif file_path.endswith('.rar'):
            with rarfile.RarFile(file_path, 'r') as rar_ref:
                rar_ref.testrar()
            return True
        return False
    except:
        return False

def move_file_to_folder(file_path, folder_name):
    destination_folder = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    file_name = os.path.basename(file_path)
    destination_file_path = os.path.join(destination_folder, file_name)
    
    if os.path.exists(destination_file_path):
        reply = QMessageBox.question(None, 'File Exists', f'A file named {file_name} already exists. Do you want to replace it?', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return False
    
    try:
        shutil.move(file_path, destination_file_path)
        return True
    except Exception as e:
        print(f"Error moving file: {e}")
        return False

def is_file_valid(file_path):
    folder_name = get_folder_for_file(file_path)
    if folder_name == 'images' and is_image(file_path):
        return True
    elif folder_name == 'texts' and is_text(file_path):
        return True
    elif folder_name == 'pdfs' and is_pdf(file_path):
        return True
    elif folder_name == 'audio' and is_audio(file_path):
        return True
    elif folder_name == 'videos' and is_video(file_path):
        return True
    elif folder_name == 'archives' and is_archive(file_path):
        return True
    elif folder_name == 'documents':
        return True
    elif folder_name == 'excel':
        return True
    elif folder_name == 'presentations':
        return True
    elif folder_name == 'web':
        return True
    elif folder_name == 'code':
        return True
    elif folder_name == 'executables':
        return True
    return False
