from sys import argv
from itertools import combinations
from dataclasses import dataclass


row_to_expands: list[int] = []
col_to_expands: list[int] = []


@dataclass
class Galaxy:
  x: int
  y: int


def shortest_path(galaxy_0: Galaxy, galaxy_1: Galaxy, expand_rate: int) -> int:
  if galaxy_0.x < galaxy_1.x:
    expand_row_count = len(list(filter(lambda r: galaxy_0.x < r < galaxy_1.x, row_to_expands)))
  else:
    expand_row_count = len(list(filter(lambda r: galaxy_1.x < r < galaxy_0.x, row_to_expands)))
  if galaxy_0.y < galaxy_1.y:
    expand_col_count = len(list(filter(lambda c: galaxy_0.y < c < galaxy_1.y, col_to_expands)))
  else:
    expand_col_count = len(list(filter(lambda c: galaxy_1.y < c < galaxy_0.y, col_to_expands)))
  return abs(galaxy_0.x - galaxy_1.x) + abs(galaxy_0.y - galaxy_1.y) + expand_rate * (expand_row_count + expand_col_count) - (expand_row_count + expand_col_count)


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    image: list[str] = file.readlines()
    for idx, row in enumerate(image):
      if row.count("#") == 0:
        row_to_expands.append(idx)
    for j in range(len(image[0])):
      if all(row[j] == "." for row in image):
        col_to_expands.append(j)
    galaxies: list[Galaxy] = []
    for i in range(len(image)):
      for j in range(len(image[i])):
        if image[i][j] == "#":
          galaxies.append(Galaxy(i, j))
    print("Part One:", sum(shortest_path(g[0], g[1], expand_rate=2) for g in combinations(galaxies, 2)))
    print("Part Two:", sum(shortest_path(g[0], g[1], expand_rate=1000000) for g in combinations(galaxies, 2)))
