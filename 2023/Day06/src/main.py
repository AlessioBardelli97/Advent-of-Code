from sys import argv


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    times = list(map(int, file.readline().split()[1:]))
    distances = list(map(int, file.readline().split()[1:]))
    part_one = 1
    part_two = 0
    for time, distance in zip(times, distances):
      ways = 0
      for t in range(time+1):
        t_rimanente = time - t
        distanza_percorsa = t * t_rimanente
        if distanza_percorsa > distance:
          ways += 1
      part_one *= ways
    print("Part One:", part_one)
    time = int("".join(map(str, times)))
    distance = int("".join(map(str, distances)))
    for t in range(time+1):
      t_rimanente = time - t
      distanza_percorsa = t * t_rimanente
      if distanza_percorsa > distance:
        part_two += 1
    print("Part Two:", part_two)
