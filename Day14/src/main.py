from sys import argv
from math import inf


class Coord:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    @classmethod
    def parse(cls, coord: str) -> "Coord":
        x, y = coord.split(",")
        return cls(int(x), int(y))
    def __repr__(self) -> str:
        return f"Coord(x={self.x}, y={self.y})"
    def copy(self) -> "Coord":
        return Coord(self.x, self.y)
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Coord):
            return False
        return (self.x, self.y) == (__value.x, __value.y)


class PathShape:
    def __init__(self, scan: str) -> None:
        self.paths = list(map(Coord.parse, scan.split(" -> ")))
    def __repr__(self) -> str:
        return "[" + ", ".join(map(repr, self.paths)) + "]"


class Cave:
    def __init__(self) -> None:
        self.cave = dict()
        self.sandSource = Coord(500, 0)
        self.start_floor = 0
    def getStartAbyss(self) -> Coord:
        return max(self.cave.keys(), key=lambda c: c.y)
    def setStartFloor(self) -> None:
        self.start_floor = self.getStartAbyss().y + 2
    def addPathShape(self, pathShape: PathShape) -> None:
        for idx in range(1, len(pathShape.paths)):
            start = pathShape.paths[idx-1]
            end = pathShape.paths[idx]
            if start.x == end.x:
                if start.y > end.y:
                    start, end = end, start
                for i in range(start.y, end.y + 1):
                    self.cave[Coord(start.x, i)] = "#"
            elif start.y == end.y:
                if start.x > end.x:
                    start, end = end, start
                for i in range(start.x, end.x + 1):
                    self.cave[Coord(i, start.y)] = "#"
    def sandComesToRest(self) -> bool:
        sand = self.sandSource.copy()
        sand_comes_to_rest = False
        flowing_into_abyss = False
        start_abyss = self.getStartAbyss()
        while not sand_comes_to_rest and not flowing_into_abyss:
            if Coord(sand.x, sand.y + 1) not in self.cave:
                sand.y += 1
                if sand.y > start_abyss.y:
                    flowing_into_abyss = True
            elif Coord(sand.x - 1, sand.y + 1) not in self.cave:
                sand.x -= 1
                sand.y += 1
            elif Coord(sand.x + 1, sand.y + 1) not in self.cave:
                sand.x += 1
                sand.y += 1
            else:
                sand_comes_to_rest = True
        if sand_comes_to_rest and not flowing_into_abyss:
            self.cave[Coord(sand.x, sand.y)] = "o"
        return sand_comes_to_rest
    def sandComesToRestWithFloor(self) -> bool:
        sand = self.sandSource.copy()
        sand_comes_to_rest = False
        while not sand_comes_to_rest:
            if Coord(sand.x, sand.y + 1) not in self.cave:
                sand.y += 1
                if sand.y + 1 == self.start_floor:
                    sand_comes_to_rest = True
            elif Coord(sand.x - 1, sand.y + 1) not in self.cave:
                sand.x -= 1
                sand.y += 1
                if sand.y + 1 == self.start_floor:
                    sand_comes_to_rest = True
            elif Coord(sand.x + 1, sand.y + 1) not in self.cave:
                sand.x += 1
                sand.y += 1
                if sand.y + 1 == self.start_floor:
                    sand_comes_to_rest = True
            else:
                sand_comes_to_rest = True
        if sand_comes_to_rest:
            self.cave[Coord(sand.x, sand.y)] = "o"
            if sand.y == self.sandSource.y:
                sand_comes_to_rest = False
        return sand_comes_to_rest


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        lines = file.read().split("\n")
        pathShapes = [PathShape(line) for line in lines]
        cave = Cave()
        for pathShape in pathShapes:
            cave.addPathShape(pathShape)
        count = 0
        cave.setStartFloor()
        while cave.sandComesToRest():
            count += 1
        print("Part One:", count)
        while cave.sandComesToRestWithFloor():
            count += 1
        print("Part Two:", count+1)
