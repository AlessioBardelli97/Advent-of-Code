from sys import argv
from collections import Counter
from re import findall


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    two_count, three_count = 0, 0
    lines = file.readlines()
    all_lines = "".join(lines)
    for line in lines:
      char_count = Counter(line)
      if any(count == 2 for count in char_count.values()):
        two_count += 1
      if any(count == 3 for count in char_count.values()):
        three_count += 1
      for i in range(len(line)):
        pattern = line[:i] + "." + line[i+1:]
        matches = findall(pattern, all_lines)
        if matches and len(matches) > 1:
          part_two = line[:i] + line[i+1:]
          break
    print("Part One:", two_count * three_count)
    print("Part Two:", part_two)
