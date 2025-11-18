def read_lines(file_route):
    with open(file_route, "r", encoding="utf-8") as read_file:
        return [line.strip() for line in read_file]
    
def save_lines(file_route, lines):
    with open(file_route, "w", encoding="utf-8") as save_file_lines:
        for line in lines:
            save_file_lines.write(str(line) + "\n")