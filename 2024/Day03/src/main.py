from sys import argv
from re import findall, finditer


def parse_input(lines: list[str]) -> list[str]:
  return [line[:-1] for line in lines]


def part_one(corrupted_memory: list[str]) -> int:
  result = 0
  for line_of_memory in corrupted_memory:
    matches = findall(r"mul\((\d{1,3}),(\d{1,3})\)", line_of_memory)
    result += sum(int(match[0]) * int(match[1]) for match in matches)
  return result


def part_two(corrupted_memory: list[str]) -> int:
  result = 0
  mul_instructions_are_enabled = True
  for line_of_memory in corrupted_memory:
    matches = finditer(r"mul\((\d{1,3}),(\d{1,3})\)", line_of_memory)
    mul_instructions = [{"type": "mul", "mul": m.groups(), "start": m.start()} for m in matches]

    matches = finditer(r"do\(\)", line_of_memory)
    do_instructions = [{"type": "do", "start": m.start()} for m in matches]

    matches = finditer(r"don't\(\)", line_of_memory)
    dont_instructions = [{"type": "dont", "start": m.start()} for m in matches]

    instructions = sorted(mul_instructions + do_instructions + dont_instructions, key=lambda m: m["start"])
    for instruction in instructions:
      if instruction["type"] == "mul":
        if mul_instructions_are_enabled:
          result += int(instruction["mul"][0]) * int(instruction["mul"][1])
      elif instruction["type"] == "do":
        mul_instructions_are_enabled = True
      elif instruction["type"] == "dont":
        mul_instructions_are_enabled = False
  return result


if __name__ == "__main__":
  with open(argv[1]) as file:
    corrupted_memory = parse_input(file.readlines())
    print("Part one: ", part_one(corrupted_memory))
    print("Part two: ", part_two(corrupted_memory))
