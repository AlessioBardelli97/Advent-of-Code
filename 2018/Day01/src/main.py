from sys import argv


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    old_frequency, current_frequency, i = [], 0, 0
    frequencies = [int(line) for line in file.readlines()]
    while current_frequency not in old_frequency:
      old_frequency.append(current_frequency)
      current_frequency += frequencies[i]
      i = (i + 1) % len(frequencies)
    print("Part One:", sum(frequencies))
    print("Part Two:", current_frequency)
