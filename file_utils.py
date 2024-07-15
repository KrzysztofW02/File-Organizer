import os
import shutil
from PIL import Image
from PyPDF2 import PdfFileReader
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
    '.doc': 'word',
    '.docx': 'word',
    '.odt': 'word',
    '.ppt': 'powerpoint',
    '.pptx': 'powerpoint',
    '.pps': 'powerpoint',
    '.ppsx': 'powerpoint',
    '.odp': 'powerpoint',
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
    shutil.move(file_path, destination_folder)

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
    return False
