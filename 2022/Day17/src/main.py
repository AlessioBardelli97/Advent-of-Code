from sys import argv
from re import findall


type Sensor = list[int]


def md(p, q): return abs(p[0] - q[0]) + abs(p[1] - q[1])


def parse_line(line: str) -> Sensor:
    return list(map(int, findall(r"-?\d+", line)))


def part_one(sensors: list[Sensor], row: int) -> int:
    beaconInRow = set()
    beaconCannotExistPositions = set()
    for sensor in sensors:
        if sensor[3] == row:
            beaconInRow.add(sensor[2])
        manhattanDistance = md(sensor[:2], sensor[2:])
        if ((sensor[1] <= row) and (sensor[1] + manhattanDistance >= row)) or\
           ((sensor[1] >  row) and (sensor[1] - manhattanDistance <= row)):
            offsetX = manhattanDistance - abs(sensor[1] - row)
            for i in range(offsetX + 1):
                beaconCannotExistPositions.add(sensor[0] + i)
                beaconCannotExistPositions.add(sensor[0] - i)
    return len(beaconCannotExistPositions - beaconInRow)


def part_two(sensors: list[Sensor], bound: int) -> int:
    acoeffs, bcoeffs = set(), set()
    radius = {(sx, sy): md((sx, sy), (bx, by)) for sx, sy, bx, by in sensors}
    scanners = radius.keys()
    for ((x,y), r) in radius.items():
        acoeffs.add(y - x + r + 1)
        acoeffs.add(y - x - r - 1)
        bcoeffs.add(x + y + r + 1)
        bcoeffs.add(x + y - r - 1)
    for a in acoeffs:
        for b in bcoeffs:
            p = ((b - a) // 2, (a + b) // 2)
            if all(0 < c < bound for c in p):
                if all(md(p, t) > radius[t] for t in scanners):
                    return 4_000_000 * p[0] + p[1]
    return 0


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        lines = file.read().split("\n")
    sensors = list(map(parse_line, lines))
    print("Part One:", part_one(sensors, 2_000_000))
    print("Part Two:", part_two(sensors, 4_000_000))
