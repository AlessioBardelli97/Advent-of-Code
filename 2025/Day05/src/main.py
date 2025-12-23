from sys import argv


def parse_input(lines: list[str]) -> tuple[list[tuple[int, int]], list[int]]:

  fresh_ids_range: list[tuple[int, int]] = []

  i = 0
  while i < len(lines) and lines[i] != "\n":
    ids = lines[i].split("-")
    fresh_ids_range.append((int(ids[0]), int(ids[1])))
    i += 1

  return fresh_ids_range, list(map(int, lines[i+1:]))


def part_one(fresh_ids_range: list[tuple[int, int]], avail_ids: list[int]) -> int:
  result = 0
  for avail_id in avail_ids:
    for fresh_id_range in fresh_ids_range:
      if fresh_id_range[0] <= avail_id <= fresh_id_range[1]:
        result += 1
        break
  return result


def range_overlap(range_1: tuple[int, int], range_2: tuple[int, int]) -> bool:
  if range_1[1] >= range_2[0]:
    return True
  return False


def merge_range(range_1: tuple[int, int], range_2: tuple[int, int]) -> tuple[int, int]:
  return min(range_1[0], range_2[0]), max(range_1[1], range_2[1])


def part_two(fresh_ids_range: list[tuple[int, int]]) -> int:
  copy_of_fresh_ids_range, i = sorted(fresh_ids_range, key=lambda x: x[0]), 0
  while i < len(copy_of_fresh_ids_range) - 1:
    if range_overlap(copy_of_fresh_ids_range[i], copy_of_fresh_ids_range[i+1]):
      copy_of_fresh_ids_range[i] = merge_range(copy_of_fresh_ids_range[i], copy_of_fresh_ids_range[i+1])
      del copy_of_fresh_ids_range[i+1]
    else:
      i += 1
  return sum(fresh_id_range[1] - fresh_id_range[0] + 1 for fresh_id_range in copy_of_fresh_ids_range)


if __name__ == "__main__":
  with open(argv[1]) as file:
    fresh_ids_range, avail_ids = parse_input(file.readlines())
    print("Part one: ", part_one(fresh_ids_range, avail_ids))
    print("Part two: ", part_two(fresh_ids_range))
