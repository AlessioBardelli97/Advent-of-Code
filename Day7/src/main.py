from sys import argv


file_system = {
    "/": {
        "a": {
            "e": {
                "i": 584
            },
            "f": 29116,
            "g": 2557,
            "h.lst": 62596
        },
        "b.txt": 14848514,
        "c.dat": 8504156,
        "d": {
            "j": 4060174,
            "d.log": 8033020,
            "d.ext": 5626152,
            "k": 7214296
        }
    }
}


file_system = {}
current_directory = "/a/e"


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        terminal_output = file.read()
        for line in terminal_output.split("\n"):
            if line[0] == "$":
                pass # E' un comando
            else:
                pass # E' output del comando precedente
