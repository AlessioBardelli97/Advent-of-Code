from math import prod
from sys import argv


def is_symbol(i: int, j: int, engineSchematic: list[str]) -> bool:
  return engineSchematic[i][j] != "." and not engineSchematic[i][j].isdigit() and engineSchematic[i][j] != "\n"


def get_number_end(i: int, j: int, engineSchematic: list[str]) -> int:
  number_end = j
  while number_end+1 < len(engineSchematic[i]) and engineSchematic[i][j:number_end+1].isdigit():
    number_end += 1
  return number_end


def get_number_start(i: int, j: int, engineSchematic: list[str]) -> int:
  number_start = j
  while number_start-1 >= 0 and engineSchematic[i][number_start-1:j].isdigit():
    number_start -= 1
  return number_start


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    engine_schematic = file.readlines()
    partOne = 0
    partTwo = 0
    for i in range(len(engine_schematic)):
      j = 0
      while j < len(engine_schematic[i]):
        if engine_schematic[i][j].isdigit():
          part_number_end = get_number_end(i, j, engine_schematic)
          part_number = int(engine_schematic[i][j:part_number_end])
          for k in range(j, part_number_end):
            if i-1 >= 0 and k-1 >= 0 and is_symbol(i-1, k-1, engine_schematic):
              partOne += part_number
              break
            if i-1 >= 0 and is_symbol(i-1, k, engine_schematic):
              partOne += part_number
              break
            if i-1 >= 0 and k+1 < len(engine_schematic[i-1]) and is_symbol(i-1, k+1, engine_schematic):
              partOne += part_number
              break
            if k-1 >= 0 and is_symbol(i, k-1, engine_schematic):
              partOne += part_number
              break
            if k+1 < len(engine_schematic[i]) and is_symbol(i, k+1, engine_schematic):
              partOne += part_number
              break
            if i+1 < len(engine_schematic) and k-1 >= 0 and is_symbol(i+1, k-1, engine_schematic):
              partOne += part_number
              break
            if i+1 < len(engine_schematic) and is_symbol(i+1, k, engine_schematic):
              partOne += part_number
              break
            if i+1 < len(engine_schematic) and k+1 < len(engine_schematic[i+1]) and is_symbol(i+1, k+1, engine_schematic):
              partOne += part_number
              break
          j = part_number_end+1
        elif engine_schematic[i][j] == "*":
          part_numbers = []
          if i-1 >= 0 and j-1 >= 0 and engine_schematic[i-1][j-1].isdigit():
            part_number_start = get_number_start(i-1, j-1, engine_schematic)
            part_numbers.append(int(engine_schematic[i-1][part_number_start:j]))            
          if i-1 >= 0 and engine_schematic[i-1][j].isdigit():
            part_number_start = get_number_start(i-1, j, engine_schematic)
            part_numbers.append(int(engine_schematic[i-1][part_number_start:j+1]))            
          if i-1 >= 0 and j+1 < len(engine_schematic[i-1]) and engine_schematic[i-1][j+1].isdigit():
            part_number_start = get_number_start(i-1, j+1, engine_schematic)
            part_numbers.append(int(engine_schematic[i-1][part_number_start:j+2]))            
          if j-1 >= 0 and engine_schematic[i][j-1].isdigit():
            part_number_start = get_number_start(i, j-1, engine_schematic)
            part_numbers.append(int(engine_schematic[i][part_number_start:j]))            
          if j+1 < len(engine_schematic[i]) and engine_schematic[i][j+1].isdigit():
            part_number_start = get_number_start(i, j+1, engine_schematic)
            part_numbers.append(int(engine_schematic[i][part_number_start:j+2]))            
          if i+1 < len(engine_schematic) and j-1 >= 0 and engine_schematic[i+1][j-1].isdigit():
            part_number_start = get_number_start(i+1, j-1, engine_schematic)
            part_numbers.append(int(engine_schematic[i+1][part_number_start:j]))            
          if i+1 < len(engine_schematic) and engine_schematic[i+1][j].isdigit():
            part_number_start = get_number_start(i+1, j, engine_schematic)
            part_numbers.append(int(engine_schematic[i+1][part_number_start:j+1]))            
          if i+1 < len(engine_schematic) and j+1 < len(engine_schematic[i+1]) and engine_schematic[i+1][j+1].isdigit():
            part_number_start = get_number_start(i+1, j+1, engine_schematic)
            part_numbers.append(int(engine_schematic[i+1][part_number_start:j+2]))            
          if len(part_numbers) == 2:
            partTwo += prod(part_numbers)
          j += 1
        else:
          j += 1
        
  print("Part One:", partOne)
