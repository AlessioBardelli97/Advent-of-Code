if __name__ == "__aoc2022__":
    if "input_file" not in locals():
        print("Error: pass an input file")
    else:
        calories = [0]
        with locals()["input_file"].open() as file:
            for line in file.readlines():
                if line == "\n":
                    calories.append(0)
                else:
                    calories[-1] += int(line)
        print("  Part One:", sum(sorted(calories, reverse=True)))
        print("  Part Two:", sum(sorted(calories, reverse=True)[:3]))
