from sys import argv
from re import search


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    partOne = 0
    original_and_copied: dict[int, int] = {}
    for card, line in enumerate(file.readlines(), 1):
      if card not in original_and_copied:
        original_and_copied[card] = 1
      else:
        original_and_copied[card] += 1
      points = 0
      winning_number, numbers_you_have = [nums.split() for nums in search(":(.*)\\|(.*)", line).group(1, 2)]
      copy = card
      for number_you_have in numbers_you_have:
        if number_you_have in winning_number:
          copy += 1
          if copy not in original_and_copied:
            original_and_copied[copy] = 1
          else:
            original_and_copied[copy] += original_and_copied[card]
          if points == 0:
            points = 1
          else:
            points *= 2
      partOne += points
    partTwo = sum(original_and_copied[k] for k in original_and_copied)
  print("Part One:", partOne)
  print("Part Two:", partTwo)
