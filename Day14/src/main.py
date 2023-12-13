from sys import argv


class Coord:
    def __init__(self, coord: str) -> None:
        x, y = coord.split(",")
        self.x = int(x)
        self.y = int(y)

class PathShape:
    def __init__(self, scan: str) -> None:
        self.paths = list(map(Coord, scan.split(" -> ")))


class Rocks:
    def __init__(self) -> None:
        self.rocks = [["." for _ in range(10)] for _ in range(10)]
    def __str__(self) -> str:
        return "\n".join("".join(rock) for rock in self.rocks)
    def addPathShape(self, pathShape: PathShape) -> None:
        for coord in pathShape.paths:
            pass


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        lines = file.read().split("\n")
        pathShapes = [PathShape(line) for line in lines]
        rocks = Rocks()
        print(rocks)
        for pathShape in pathShapes:
            rocks.addPathShape(pathShape)
        print(rocks)
