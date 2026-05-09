from pathlib import Path
from ingestion import *

def main():
    file = read_log_file("./app.log")
    parser = logParser()
    for value in file:
         data = parser.parse(value)
         print(data)




if __name__ == "__main__":
    main()
