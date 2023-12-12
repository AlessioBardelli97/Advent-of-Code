from sys import argv


class Head:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
    def move(self, direction: str):
        if direction == "U":
            self.y += 1
        elif direction == "R":
            self.x += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "L":
            self.x -= 1


class Knot:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
    def move_toward(self, previous_knot):
        if (abs(self.y - previous_knot.y) >= 2 and abs(self.x - previous_knot.x) >= 1) or \
           (abs(self.x - previous_knot.x) >= 2 and abs(self.y - previous_knot.y) >= 1):
            if self.y < previous_knot.y:
                self.y += 1
            else:
                self.y -= 1
            if self.x < previous_knot.x:
                self.x += 1
            else:
                self.x -= 1
        elif abs(self.y - previous_knot.y) == 2 and (self.x - previous_knot.x == 0):
            if self.y < previous_knot.y:
                self.y += 1
            else:
                self.y -= 1
        elif abs(self.x - previous_knot.x) == 2 and (self.y - previous_knot.y == 0):
            if self.x < previous_knot.x:
                self.x += 1
            else:
                self.x -= 1



class Rope:
    def __init__(self, knots_count: int) -> None:
        self.head = Head()
        self.knots = [Knot() for _ in range(knots_count-1)]
        self.tail_positions: set[tuple[int, int]] = {(0, 0)}
    def move(self, direction: str):
        self.head.move(direction)
        for i in range(len(self.knots)):
            if i >= 1:
                self.knots[i].move_toward(self.knots[i-1])
            else:
                self.knots[0].move_toward(self.head)
        tail = self.knots[-1]
        self.tail_positions.add((tail.x, tail.y))
    def len_tail_positions(self) -> int:
        return len(self.tail_positions)


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        motions = file.read().split("\n")
        rope2 = Rope(2)
        rope10 = Rope(10)
        for motion in motions:
            direction, times = motion.split(" ")
            for _ in range(int(times)):
                rope2.move(direction)
                rope10.move(direction)
        print("Part One:", rope2.len_tail_positions())
        print("Part Two:", rope10.len_tail_positions())
