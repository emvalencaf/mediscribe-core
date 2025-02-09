from pathlib import Path
import shutil

from fastapi import UploadFile

def load_file(file: UploadFile) -> Path:
    """
    Loads a file to the server and saves it in the 'uploaded_files' directory.

    :param file: The file to be uploaded, provided as an UploadFile object.
    :return: The location where the file has been saved.
    """
    root_folder = Path(__file__).parent
    
    upload_folder = root_folder / "uploaded_files"
    
    upload_folder.mkdir(parents=True, exist_ok=True)
    
    file_location = upload_folder / file.filename
    
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)
        
    return file_location


def load_txt_file(content: str, filename: str,
                  partition: str = "transcribed_files") -> Path:
    """
    Saves the provided text content as a .txt file in the specified folder.

    :param content: The content to be written to the file.
    :param filename: The name of the file to be created.
    :param partition: The folder in which the file will be saved (default is 'transcribed_files').
    :return: The location where the .txt file has been saved.
    """
    root_folder = Path(__file__).parent.parent
    
    upload_folder = root_folder / partition
    
    upload_folder.mkdir(parents=True, exist_ok=True)
    
    file_location = upload_folder / filename
    
    with open(file_location, "w", encoding="utf-8") as f:
        f.write(content)
        
    return file_location
