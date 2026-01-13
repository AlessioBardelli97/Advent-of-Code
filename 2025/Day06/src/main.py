from sys import argv
from functools import reduce
from operator import  mul


class Problem:

  def __init__(self):
    self.numbers = []
    self.operation = ""

  def __repr__(self):
    return f"Problem(numbers={self.numbers}, operation={self.operation})"

  def resolve(self) -> int:
    if self.operation == "+":
      return sum(self.numbers)
    elif self.operation == "*":
      return reduce(mul, self.numbers)
    else:
      raise Exception(f"Invalid operation: {self.operation}")


def parse_input(lines: list[str]) -> list[Problem]:
  result = []
  for line in lines:
    for idx, column in enumerate(line.split()):
      if len(result) == idx:
        result.append(Problem())
      if column.isdigit():
        result[idx].numbers.append(int(column))
      elif column in ["+", "*"]:
        result[idx].operation = column

  for i in range(len(lines)):
    for j in range(len(lines[i])):
      pass
  return result


def part_one(problems: list[Problem]) -> int:
  return sum(problem.resolve() for problem in problems)


def part_two(problems: list[Problem]) -> int:
  result = 0
  return result


if __name__ == "__main__":
  with open(argv[1]) as file:
    problems = parse_input(file.readlines())
    print("Part one: ", part_one(problems))
    print("Part two: ", part_two(problems))
