from sys import argv


def parse_input(lines: list[str]) -> list[list[str]]:
  return [list(line[:-1]) for line in lines]


def can_access_roll_of_paper(i: int, j: int, rolls_of_paper: list[list[str]]) -> bool:
  result, rolls_of_paper_in_the_adjacent_positions = False, 0

  if rolls_of_paper[i][j] == "@":

    # ↖
    if i - 1 >= 0 and j - 1 >= 0 and rolls_of_paper[i - 1][j - 1] == "@":
      rolls_of_paper_in_the_adjacent_positions += 1

    # ↑
    if i - 1 >= 0 and rolls_of_paper[i - 1][j] == "@":
      rolls_of_paper_in_the_adjacent_positions += 1

    # ↗
    if i - 1 >= 0 and j + 1 < len(rolls_of_paper[i]) and rolls_of_paper[i - 1][j + 1] == "@":
      rolls_of_paper_in_the_adjacent_positions += 1

    # →
    if j + 1 < len(rolls_of_paper[i]) and rolls_of_paper[i][j + 1] == "@":
      rolls_of_paper_in_the_adjacent_positions += 1

    # ↘
    if i + 1 < len(rolls_of_paper) and j + 1 < len(rolls_of_paper[i]) and rolls_of_paper[i + 1][j + 1] == "@":
      rolls_of_paper_in_the_adjacent_positions += 1

    # ↓
    if i + 1 < len(rolls_of_paper) and rolls_of_paper[i + 1][j] == "@":
      rolls_of_paper_in_the_adjacent_positions += 1

    # ↙
    if i + 1 < len(rolls_of_paper) and j - 1 >= 0 and rolls_of_paper[i + 1][j - 1] == "@":
      rolls_of_paper_in_the_adjacent_positions += 1

    # ←
    if j - 1 >= 0 and rolls_of_paper[i][j - 1] == "@":
      rolls_of_paper_in_the_adjacent_positions += 1

    if rolls_of_paper_in_the_adjacent_positions < 4:
      result = True

  return result


def part_one(rolls_of_paper: list[list[str]]) -> int:
  result = 0
  for i in range(len(rolls_of_paper)):
    for j in range(len(rolls_of_paper[i])):
      if can_access_roll_of_paper(i, j, rolls_of_paper):
          result += 1
  return result


def part_two(rolls_of_paper: list[list[str]]) -> int:
  result, have_roll_to_remove = 0, True
  while have_roll_to_remove:
    rolls_to_remove: list[tuple[int, int]] = []
    for i in range(len(rolls_of_paper)):
      for j in range(len(rolls_of_paper[i])):
        if can_access_roll_of_paper(i, j, rolls_of_paper):
          rolls_to_remove.append((i, j))
    if len(rolls_to_remove) > 0:
      result += len(rolls_to_remove)
      for roll_to_remove in rolls_to_remove:
        rolls_of_paper[roll_to_remove[0]][roll_to_remove[1]] = "."
    else:
      have_roll_to_remove = False
  return result


if __name__ == "__main__":
  with open(argv[1]) as file:
    rolls_of_paper = parse_input(file.readlines())
    print("Part one: ", part_one(rolls_of_paper))
    print("Part two: ", part_two(rolls_of_paper))
