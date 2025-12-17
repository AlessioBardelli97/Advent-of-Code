from dataclasses import dataclass
from sys import argv


@dataclass
class Rotation:
  direction: str
  distance: int
  @classmethod
  def from_string(cls, line: str) -> "Rotation":
    return cls(line[0], int(line[1:-1]))


def parse_input(lines: list[str]) -> list[Rotation]:
  return [Rotation.from_string(line) for line in lines]


def part_one(rotations: list[Rotation]) -> int:
  dial, zero_count = 50, 0
  for rotation in rotations:
    if rotation.direction == "L":
      dial = (dial - rotation.distance) % 100
    elif rotation.direction == "R":
      dial = (dial + rotation.distance) % 100
    if dial == 0:
      zero_count += 1
  return zero_count


def part_two(rotations: list[Rotation]) -> int:
  dial, zero_count = 50, 0
  for rotation in rotations:
    if rotation.direction == 'L':
      if dial == 0:
        dist_to_first_zero = 100
      else:
        dist_to_first_zero = dial
    elif rotation.direction == 'R':
      if dial == 0:
        dist_to_first_zero = 100
      else:
        dist_to_first_zero = 100 - dial
    else:
      raise Exception()

    if rotation.distance >= dist_to_first_zero:
      zero_count += 1 + ((rotation.distance - dist_to_first_zero) // 100)

    if rotation.direction == "L":
      dial = (dial - rotation.distance) % 100
    elif rotation.direction == "R":
      dial = (dial + rotation.distance) % 100
  return zero_count


if __name__ == "__main__":
  with open(argv[1]) as file:
    rotations = parse_input(file.readlines())
    print("Part one: ", part_one(rotations))
    print("Part two: ", part_two(rotations))
