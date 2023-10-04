import sys
from pathlib import Path
import zipfile
import tarfile

CATEGORIES = {"Audio": [".mp3",],
              "Video": [".mp4"],
              "Fotos": [".jpg"],
              "Docs": [".rtf", ".txt", ".bmp", '.pdf'],
              "Archives": [".zip", ".wim", ".tar"]
              }

def get_categories(file:Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat                
    return "Other"  

def move_file(file:Path, category:str, root_dir:Path) -> None:
    target_dir = root_dir.joinpath(category)
    print(target_dir.exists())
    if not target_dir.exists():
        target_dir.mkdir()
            
    file.replace(target_dir.joinpath(file.name))    
        
    
def sort_folder(path:Path) -> None:
    
    for element in path.glob("**/*"):
        if element.is_file():
            category = get_categories(element)
            move_file(element, category, path)
            
    for dir_path in path.glob('**/*'):
        if dir_path.is_dir() and not any(dir_path.iterdir()):
            dir_path.rmdir()        
            
            

def extract_and_move_archives(file_path, destination_folder):
    file_extension = file_path.suffix.lower()
    if file_extension == '.zip':
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)
    elif file_extension == '.wim':
        with wimfile.open(file_path, 'r:wim') as wim_ref:
            wim_ref.extractall(destination_folder)
    elif file_extension == '.tar':
        with tarfile.open(file_path, 'r') as tar_ref:
            tar_ref.extractall(destination_folder)
            
            
def main() -> str:
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"
                
    if not path.exists():
        return "Folder dos not exists"
    
    sort_folder(path)
                
    return "All ok"

if __name__ == "__main__":
    print(main())