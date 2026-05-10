from pathlib import Path
from ingestion import *
from transfrom import *
from load_logs import load_log


def main():
    file = read_log_file("./app.log")
    parser = logParser()
    for value in file:
        data = parser.parse(value)
        striped_line = remove_whitespace(data)
        normalize_level = normalize_log_level(striped_line)
        cleaned_time = convert_time(normalize_level)
        yield cleaned_time


if __name__ == "__main__":
    load_log(main())
