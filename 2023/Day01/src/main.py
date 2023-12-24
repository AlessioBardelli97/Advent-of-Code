from sys import argv
from re import findall


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        lines = file.readlines()
        print("Part One:", sum([int(val[0] + val[-1]) for val in [findall(r"\d", line) for line in lines]]))
        _sum = 0
        convert = {
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
        }
        for line in lines:
            min_idxs: list[tuple[str, int]] = []
            max_idxs: list[tuple[str, int]] = []
            for key in convert:
                line = line.replace(key, convert[key])
            for key in convert:
                result = line.find(convert[key])
                if result != -1:
                    min_idxs.append((key, result))
                result = line.rfind(convert[key])
                if result != -1:
                    max_idxs.append((key, result))
            _min = min(min_idxs, key=lambda x: x[1])
            _max = max(max_idxs, key=lambda x: x[1])
            _sum += int(_min[0] + _max[0])
        print("Part Two:", _sum)
