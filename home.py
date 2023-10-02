import sys
from pathlib import Path

def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"
                    
    if not path.exists():
        return "Folder dos not exists"
        
    return "All OK"
    
if __name__ == "__main__":
    print(main())