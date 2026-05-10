from datetime import datetime

def remove_whitespace(line):
    for element in line:
        cleaned = line[element].strip()
        line[element] = cleaned
    return line


def normalize_log_level(line):
    level = line.get("level", "")
    if level == "":
        raise "log level not found"
    normalized =  line["level"].upper()
    line["level"] = normalized
    return line


def convert_time(line):
    time_element = line.get("timestamp","")
    if time_element == "":
        raise "log timestamp not found"
    clean_time = datetime.strptime(line["timestamp"], "%Y-%m-%d %H:%M:%S")
    line["timestamp"] = clean_time
    return line
    