from sys import argv


if __name__ == "__main__" and len(argv) >= 2:
    calories = [0]
    with open(argv[1]) as file:
        for line in file.readlines():
            if line == "\n":
                calories.append(0)
            else:
                calories[-1] += int(line)
    print("  Part One:", sum(sorted(calories, reverse=True)))
    print("  Part Two:", sum(sorted(calories, reverse=True)[:3]))
