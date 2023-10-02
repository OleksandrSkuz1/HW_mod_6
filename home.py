import sys
from pathlib import Path


def sort_folder(path:Path, elements=[]) -> None:
    for item in path.iterdir():
        if item.is_dir():
            sort_folder(item, elements)
        else:
            elements.append(item) 
    print(elements)        

def main() -> str: 
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"
                    
    if not path.exists():
        return "Folder dos not exists"
    
    sort_folder(path)
        
    return "All OK"
    
if __name__ == "__main__":
    print(main())