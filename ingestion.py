from pathlib import Path


def read_log_file(file_path):

    file_dir = Path(file_path)
    if file_dir.is_dir():
        for filepath in file_dir.glob("*.log"):
            with open(filepath, "r") as file:
                for line in file:
                    clean_line = line.strip()
                    yield clean_line
    
    elif file_dir.is_file():
        filepath = file_path
        with open(filepath, "r") as file:
            for line in file:
                yield line.strip()

    else:
        raise FileNotFoundError(f"Path does not exit: {filepath}")
