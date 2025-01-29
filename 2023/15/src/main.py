from sys import argv

def hash(s: str):
  result = 0
  for c in s:
    result += ord(c)
    result *= 17
    result %= 256
  return result


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    initialization_sequence: list[str] = file.readline().split(",")[:-1]
    print("Part One:", sum(map(hash, initialization_sequence)))
