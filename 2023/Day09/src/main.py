from sys import argv


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    part_one, part_two = 0, 0
    for line in file.readlines():
      history: list[int] = list(map(int, line.split()))
      differences: list[list[int]] = [history]
      while any(d != 0 for d in differences[-1]):
        differences.append([])
        for i in range(1, len(differences[-2])):
          differences[-1].append(differences[-2][i] - differences[-2][i-1])
      differences_part_one = differences[:]
      differences_part_two = differences[:]
      differences_part_one[-1].append(0)
      differences_part_two[-1].insert(0, 0)
      for i in range(len(differences_part_one)-2, -1, -1):
        differences_part_one[i].append(differences_part_one[i][-1] + differences_part_one[i+1][-1])
        differences_part_two[i].insert(0, differences_part_two[i][0] - differences_part_two[i+1][0])
      part_one += differences_part_one[0][-1]
      part_two += differences_part_two[0][0]
    print("Part One:", part_one)
    print("Part Two:", part_two)
