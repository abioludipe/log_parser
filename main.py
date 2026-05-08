from pathlib import Path
from ingestion import *

def main():
    file = read_log_file("./app.log")
    for value in file:
        print(value)  # 0, 2, 4, 6, 8




if __name__ == "__main__":
    main()
