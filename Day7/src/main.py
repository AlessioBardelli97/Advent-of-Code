from sys import argv


def get_dir_size(directory: dict, all_dir_size: list[int]) -> int:
    tot_size = 0
    for node in directory.values():
        if type(node) == int:
            tot_size += node
        else:
            tot_size += get_dir_size(node, all_dir_size)
    all_dir_size.append(tot_size)
    return tot_size


def is_command(line: str) -> bool:
    return line.startswith("$ ")


def exec_command(line: str) -> None:
    if line[2:4] == "cd":
        if line[5:] == "..":
            current_path.pop()
        else:
            current_path.append(line[5:])
    elif line[2:4] == "ls":
        pass


def is_directory(line: str) -> bool:
    return line.startswith("dir ")


def go_to_current_directory() -> dict:
    temp_directory = file_system
    for directory in current_path:
        temp_directory = temp_directory[directory]
    return temp_directory


def add_directory_to_current_path(line: str) -> None:
    current_directory = go_to_current_directory()
    current_directory[line[4:]] = {}


def add_file_to_current_path(line: str) -> None:
    current_directory = go_to_current_directory()
    size, file_name = line.split(" ")
    current_directory[file_name] = int(size)


file_system = {}
current_path = []


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        terminal_output = file.read()
        for line in terminal_output.split("\n")[1:]:
            if is_command(line):
                exec_command(line)
            elif is_directory(line):
                add_directory_to_current_path(line)
            else:
                add_file_to_current_path(line)
        all_dir_size = []
        get_dir_size(file_system, all_dir_size)
        print("Part One:", sum(dir_size for dir_size in all_dir_size if dir_size <= 100_000))
        file_system_size = all_dir_size[-1]
        sorted(all_dir_size)
        for dir_size in all_dir_size:
            if (70000000 - file_system_size) + dir_size >= 30000000:
                print("Part Two:", dir_size)
                break
