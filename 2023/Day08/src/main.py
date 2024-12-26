from sys import argv
from re import compile, search
from math import lcm
from time import time


if __name__ == "__main__" and len(argv) >= 2:
  t1 = time()
  with open(argv[1]) as file:
    leftRightInstructions = list(map(lambda i: 0 if i == "L" else 1, file.readline()[:-1]))
    network = {}
    file.readline()
    pattern = compile(r"(.{3}) = \((.{3}), (.{3})\)")
    while line := file.readline():
      match = search(pattern, line)
      if match:
        network[match.group(1)] = (match.group(2), match.group(3))
    new_network = {}
    for k in network:
      current_key = k
      for instruction in leftRightInstructions:
        current_key = network[current_key][instruction]
      new_network[k] = current_key
    startPartOne = "AAA"
    stepPartOne = 0
    while startPartOne != "ZZZ":
      startPartOne = new_network[startPartOne]
      stepPartOne += len(leftRightInstructions)
    steps = []
    for start in filter(lambda k: k.endswith("A"), network.keys()):
      current_position = start
      steps.append(0)
      while not current_position.endswith("Z"):
        current_position = new_network[current_position]
        steps[-1] += len(leftRightInstructions)
    t2 = time()
    print("Part One:", stepPartOne)
    print("Part Two:", lcm(*steps))
    print("Solution in", round(t2-t1, 4), "seconds")
