from sys import argv


partOne = 0
partTwo = 0
maxCubes = {"red": 12, "green": 13, "blue": 14}


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    for line in file.readlines():
      line = line[:-1]
      endGameId = line.find(":")
      gameID = int(line[5:endGameId])
      foo = True
      maxRealCubeForGame = {"red": 0, "green": 0, "blue": 0}
      for subsetCubes in line[endGameId+2:].split("; "):
        for cubes in subsetCubes.split(", "):
          cubeNumber, cubeColor = cubes.split(" ")
          if int(cubeNumber) > maxCubes[cubeColor]:
            foo = False
          if int(cubeNumber) > maxRealCubeForGame[cubeColor]:
            maxRealCubeForGame[cubeColor] = int(cubeNumber)
      if foo:
        partOne += gameID
      partTwo += maxRealCubeForGame["red"] * maxRealCubeForGame["green"] * maxRealCubeForGame["blue"]

  print("Part One:", partOne)
  print("Part Two:", partTwo)
