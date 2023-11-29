def prioritie(item_type: str) -> int:
    if item_type == item_type.lower():
        return ord(item_type) - ord("a") + 1
    else:
        return ord(item_type) - ord("A") + 27


if __name__ == "__aoc2022__":
    if "input_file" not in locals():
        print("Error: pass an input file")
    else:
        with locals()["input_file"].open() as file:
            totPriorities = 0
            rucksacksContents = file.read().split("\n")
            for rucksackContent in rucksacksContents:
                size = len(rucksackContent) // 2
                firstHalf = rucksackContent[:size]
                secondHalf = rucksackContent[size:]
                for item_type in firstHalf:
                    if item_type in secondHalf:
                        totPriorities += prioritie(item_type)
                        break
            print("  Part One:", totPriorities)
            totPriorities = 0
            for i in range(0, len(rucksacksContents), 3):
                for item_type in rucksacksContents[i]:
                    if item_type in rucksacksContents[i+1] and item_type in rucksacksContents[i+2]:
                        totPriorities += prioritie(item_type)
                        break
            print("  Part Two:", totPriorities)
