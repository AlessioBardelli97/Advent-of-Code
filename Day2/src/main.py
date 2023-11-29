if __name__ == "__aoc2022__":
    if "input_file" not in locals():
        print("Error: pass an input file")
    else:
        scooresPartOne = {
            ("A", "X"): 3+1, ("A", "Y"): 6+2, ("A", "Z"): 0+3,
            ("B", "X"): 0+1, ("B", "Y"): 3+2, ("B", "Z"): 6+3,
            ("C", "X"): 6+1, ("C", "Y"): 0+2, ("C", "Z"): 3+3
        }
        scooresPartTwo = {
            ("A", "X"): 3+0, ("A", "Y"): 1+3, ("A", "Z"): 2+6,
            ("B", "X"): 1+0, ("B", "Y"): 2+3, ("B", "Z"): 3+6,
            ("C", "X"): 2+0, ("C", "Y"): 3+3, ("C", "Z"): 1+6
        }
        with locals()["input_file"].open() as file:
            totalScoorePartOne = 0
            totalScoorePartTwo = 0
            for line in file.readlines():
                totalScoorePartOne += scooresPartOne[(line[0], line[2])]
                totalScoorePartTwo += scooresPartTwo[(line[0], line[2])]
            print("  Part One:", totalScoorePartOne)
            print("  Part Two:", totalScoorePartTwo)
