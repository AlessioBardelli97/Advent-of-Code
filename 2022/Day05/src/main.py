from sys import argv


def parse_line(line):
    return line.replace("   ", "*").replace("[", "").replace("]", "").replace("\n", "")


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        cratesCrateMover9000 = [[] for _ in range(9)]
        cratesCrateMover9001 = [[] for _ in range(9)]
        operations = []
        lines = file.read().split("\n")
        idx = lines.index("")
        draw = lines[:idx-1]
        rearrangement_procedure = lines[idx+1:]
        for line in draw:
            line = parse_line(line)
            for j, crate in enumerate(line):
                if crate != "*":
                    cratesCrateMover9000[j].append(crate)
                    cratesCrateMover9001[j].append(crate)
        for line in rearrangement_procedure:
            line = line.split(" ")
            operations.append((int(line[1]), int(line[3]), int(line[5])))
        for operation in operations:
            for quantity in range(operation[0]):
                cratesCrateMover9000[operation[2]-1].insert(0, cratesCrateMover9000[operation[1]-1].pop(0))
        print("  Part One:", "".join(crate[0] for crate in cratesCrateMover9000 if len(crate) > 0))
        for operation in operations:
            temp = []
            for quantity in range(operation[0]):
                temp.append(cratesCrateMover9001[operation[1]-1].pop(0))
            temp.reverse()
            for t in temp:
                cratesCrateMover9001[operation[2]-1].insert(0, t)
        print("  Part Two:", "".join(crate[0] for crate in cratesCrateMover9001 if len(crate) > 0))
