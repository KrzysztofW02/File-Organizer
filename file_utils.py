import os
import shutil

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
    '.xls': 'spreadsheets',
    '.xlsx': 'spreadsheets',
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

def move_file_to_folder(file_path, folder_name):
    destination_folder = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(file_path, destination_folder)
