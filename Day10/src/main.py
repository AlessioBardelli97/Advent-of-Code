from sys import argv


def clock(current_cycle: int, signal_strength_cycles: dict[int, int], X: int, current_line: list[str]) -> int:
    if current_cycle % 40 == 0:
        print("".join(current_line))
    if current_cycle % 40 in [X-1, X, X+1]:
        current_line[current_cycle % 40] = "#"
    else:
        current_line[current_cycle % 40] = "."
    current_cycle += 1
    if current_cycle in signal_strength_cycles:
        signal_strength_cycles[current_cycle] = current_cycle * X
    return current_cycle


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        instructions = file.read().split("\n")
        current_cycle, X = 0, 1
        signal_strength_cycles = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}
        current_line = ["" for _ in range(40)]
        for instruction in instructions:
            if instruction == "noop":
                current_cycle = clock(current_cycle, signal_strength_cycles, X, current_line)
            else:
                current_cycle = clock(current_cycle, signal_strength_cycles, X, current_line)
                current_cycle = clock(current_cycle, signal_strength_cycles, X, current_line)
                X += int(instruction.replace("addx ", ""))
        current_cycle = clock(current_cycle, signal_strength_cycles, X, current_line)
        print("Part One:", sum(signal_strength_cycles.values()))
