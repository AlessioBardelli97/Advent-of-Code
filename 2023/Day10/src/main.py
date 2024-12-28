from sys import argv


def get_start_position(grid_of_tiles: list[str]) -> tuple[int, int]:
    i, j = 0, 0
    while grid_of_tiles[i][j] != "S":
      j += 1
      if j >= len(grid_of_tiles):
        j = 0
        i += 1
    return i, j


def explore(grid_of_tiles: list[str], node: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
  i, j = node[0], node[1]
  result: list[int] = []
  if grid_of_tiles[i][j] == "S":
    if i-1 >= 0 and grid_of_tiles[i-1][j] in ["|", "7", "F"]:
      result.extend([i-1, j])
    if j+1 < len(grid_of_tiles[i]) and grid_of_tiles[i][j+1] in ["-", "J", "7"]:
      result.extend([i, j+1])
    if i+1 < len(grid_of_tiles) and grid_of_tiles[i+1][j] in ["|", "J", "L"]:
      result.extend([i+1, j])
    if j-1 >= 0 and grid_of_tiles[i][j-1] in ["-", "F", "L"]:
      result.extend([i, j-1])
  elif grid_of_tiles[i][j] == "F":
    if j+1 < len(grid_of_tiles[i]) and grid_of_tiles[i][j+1] in ["-", "J", "7", "S"]:
      result.extend([i, j+1])
    if i+1 < len(grid_of_tiles) and grid_of_tiles[i+1][j] in ["|", "J", "L", "S"]:
      result.extend([i+1, j])
  elif grid_of_tiles[i][j] == "L":
    if i-1 >= 0 and grid_of_tiles[i-1][j] in ["|", "7", "F", "S"]:
      result.extend([i-1, j])
    if j+1 < len(grid_of_tiles[i]) and grid_of_tiles[i][j+1] in ["-", "J", "7", "S"]:
      result.extend([i, j+1])
  elif grid_of_tiles[i][j] == "J":
    if i-1 >= 0 and grid_of_tiles[i-1][j] in ["|", "7", "F", "S"]:
      result.extend([i-1, j])
    if j-1 >= 0 and grid_of_tiles[i][j-1] in ["-", "F", "L", "S"]:
      result.extend([i, j-1])
  elif grid_of_tiles[i][j] == "7":
    if i+1 < len(grid_of_tiles) and grid_of_tiles[i+1][j] in ["|", "J", "L", "S"]:
      result.extend([i+1, j])
    if j-1 >= 0 and grid_of_tiles[i][j-1] in ["-", "F", "L", "S"]:
      result.extend([i, j-1])
  elif grid_of_tiles[i][j] == "|":
    if i-1 >= 0 and grid_of_tiles[i-1][j] in ["|", "7", "F", "S"]:
      result.extend([i-1, j])
    if i+1 < len(grid_of_tiles) and grid_of_tiles[i+1][j] in ["|", "J", "L", "S"]:
      result.extend([i+1, j])
  elif grid_of_tiles[i][j] == "-":
    if j+1 < len(grid_of_tiles[i]) and grid_of_tiles[i][j+1] in ["-", "J", "7", "S"]:
      result.extend([i, j+1])
    if j-1 >= 0 and grid_of_tiles[i][j-1] in ["-", "F", "L", "S"]:
      result.extend([i, j-1])
  return (result[0], result[1]), (result[2], result[3])


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    grid_of_tiles: list[str] = list(map(lambda l: l[:-1], file.readlines()))
    start = get_start_position(grid_of_tiles)
    path: set[tuple[int, int]] = set()
    nodes_to_explore = {start}
    while nodes_to_explore:
      node_to_explore = nodes_to_explore.pop()
      path.add(node_to_explore)
      node1, node2 = explore(grid_of_tiles, node_to_explore)
      if node1 not in path:
        nodes_to_explore.add(node1)
      if node2 not in path:
        nodes_to_explore.add(node2)
    print("Part One:", len(path)//2)
