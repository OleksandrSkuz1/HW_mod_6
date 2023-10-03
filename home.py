import sys
from pathlib import Path

CATEGORIES = {"Audio": [".mp3",],
              "Video": [".mp4"],
              "Fotos": [".jpg"],
              "Docs": [".rtf", ".txt", ".bmp"]}

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