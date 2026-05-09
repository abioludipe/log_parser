from pathlib import Path
from datetime import datetime


def read_log_file(file_path):
    executed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_dir = Path(file_path)
    if file_dir.is_dir():
        for filepath in file_dir.glob("*.log"):
            with open(filepath, "r") as file:
                for line_number, line in enumerate(file):
                    clean_line = line.strip()
                    yield {
                    "source_file": file.name,
                    "line_number": line_number,
                    "raw_log": line.strip()
                }  
    
    elif file_dir.is_file():
        filepath = file_path
        with open(filepath, "r") as file:
            for line_number, line in enumerate(file):
                yield {
                    "source_file": file.name,
                    "line_number": line_number,
                    "raw_log": line.strip(),
                    "executed_at": executed_at
                }  

    else:
        raise FileNotFoundError(f"Path does not exit: {filepath}")




# Parse the line to extract the relevant data

class logParser():

    def parse(self, log):
        data = log.get("raw_log", "")
        try:
            parts = data.split("|")
            level = parts[0]
            timestamp = parts[-1]
            message = parts[1:-1]
            if len(message) == 1:
                message = message
            else:
                message = " ".join(message)
            ext_log = {"level": level,
                   "message": message,
                   "timestamp": timestamp}
        except:
            raise "log not found"
        yield  ext_log
   


