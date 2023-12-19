from math import inf
from sys import argv
from dijkstra import Graph, DijkstraSPF


type Position = tuple[int, int]


def findPosition(map: str) -> tuple[str, Position, Position]:
    lines = map.split("\n")
    start, end = (0, 0), (0, 0)
    for i in range(len(lines)):
        if (j := lines[i].find("S")) != -1:
            start = (i, j)
            lines[i] = lines[i].replace("S", "a")
        if (j := lines[i].find("E")) != -1:
            end = (i, j)
            lines[i] = lines[i].replace("E", "z")
    return "\n".join(lines), start, end


def canMove(currPos: str, newPos: str) -> bool:
    diff = ord(currPos) - ord(newPos)
    return (diff >= 0) or (diff == -1)    


def buildGraph(map: str) -> Graph:
    lines = map.split("\n")
    graph = Graph()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if j - 1 >= 0 and canMove(lines[i][j], lines[i][j-1]):
                graph.add_edge((i, j), (i, j-1), 1)
            if j + 1 < len(lines[i]) and canMove(lines[i][j], lines[i][j+1]):
                graph.add_edge((i, j), (i, j+1), 1)
            if i - 1 >= 0 and canMove(lines[i][j], lines[i-1][j]):
                graph.add_edge((i, j), (i-1, j), 1)
            if i + 1 < len(lines) and canMove(lines[i][j], lines[i+1][j]):
                graph.add_edge((i, j), (i+1, j), 1)
    return graph


def getAllStartPosition(map: str) -> list[Position]:
    positions: list[Position] = []
    lines = map.split("\n")
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "a":
                positions.append((i, j))
    return positions


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        fewestSteps = inf
        map = file.read()
        map, start, end = findPosition(map)
        graph = buildGraph(map)
        dijkstra = DijkstraSPF(graph, start)
        print("Part One:", dijkstra.get_distance(end))
        for position in getAllStartPosition(map):
            dijkstra = DijkstraSPF(graph, position)
            steps = dijkstra.get_distance(end)
            if steps < fewestSteps:
                fewestSteps = steps
        print("Part Two:", fewestSteps)
