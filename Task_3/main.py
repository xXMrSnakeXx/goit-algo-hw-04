import sys
from pathlib import Path
from colorama import Fore, Style

def visualPrint(path, space = 3):
     dirPath = Path(path)
     items = dirPath.iterdir()
     for item in items:
          if item.is_dir():
              print(f"{Fore.YELLOW}{item.name}{Style.RESET_ALL} ===>")
              visualPrint(item, space=10)
          else:
              print(f"{'-'* space}{Fore.BLUE}{item.name}{Style.RESET_ALL}") 
    
      
     
def main():
    if len(sys.argv) != 2:
        print('Usage: python main.py <directory_path>')
        sys.exit(1)
  
    dir = sys.argv[1]
    try:
        visualPrint(dir)
    except Exception as e:
        print(f"An error occured: {e}")    
 
if __name__ == "__main__" :  
 main()    
 