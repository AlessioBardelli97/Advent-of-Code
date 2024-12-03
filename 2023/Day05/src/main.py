from io import SEEK_SET
from sys import argv
import re


def parse_map(lines: list[str], i: int) -> tuple[int, list[list[int]]]:
    i, list_maps = i+1, []
    while i < len(lines) and lines[i] != "\n":
      list_maps.append(list(map(int, lines[i].split())))
      i += 1
    return i, list_maps


def find_in_map(src, list_maps):
  for list_map in list_maps:
    if list_map[1] <= src <= list_map[1]+list_map[2]:
      return (src - list_map[1]) + list_map[0]
  return src


def part2(puzzle_input):
  segments = puzzle_input.split('\n\n')
  intervals = []

  for seed in re.findall(r'(\d+) (\d+)', segments[0]):
    x1, dx = map(int, seed)
    x2 = x1 + dx
    intervals.append((x1, x2, 1))

  min_location = float('inf')
  while intervals:
    x1, x2, level = intervals.pop()
    if level == 8:
      min_location = min(x1, min_location)
      continue

    for conversion in re.findall(r'(\d+) (\d+) (\d+)', segments[level]):
      z, y1, dy = map(int, conversion)
      y2 = y1 + dy
      diff = z - y1
      if x2 <= y1 or y2 <= x1:    # no overlap
        continue
      if x1 < y1:                 # split original interval at y1
        intervals.append((x1, y1, level))
        x1 = y1
      if y2 < x2:                 # split original interval at y2
        intervals.append((y2, x2, level))
        x2 = y2
      intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
      break

    else:
      intervals.append((x1, x2, level + 1))

  return min_location


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    i, lines = 0, file.readlines()
    while i < len(lines):
      if lines[i].startswith("seeds: "):
        seeds = list(map(int, lines[i][7:].split()))
      elif lines[i].startswith("seed-to-soil map:"):
        i, seed_to_soil = parse_map(lines, i)
      elif lines[i].startswith("soil-to-fertilizer map:"):
        i, soil_to_fertilizer = parse_map(lines, i)
      elif lines[i].startswith("fertilizer-to-water map:"):
        i, fertilizer_to_water = parse_map(lines, i)
      elif lines[i].startswith("water-to-light map:"):
        i, water_to_light = parse_map(lines, i)
      elif lines[i].startswith("light-to-temperature map:"):
        i, light_to_temperature = parse_map(lines, i)
      elif lines[i].startswith("temperature-to-humidity map:"):
        i, temperature_to_humidity = parse_map(lines, i)
      elif lines[i].startswith("humidity-to-location map:"):
        i, humidity_to_location = parse_map(lines, i)
      i += 1
    locations = []
    for seed in seeds:
      soil = find_in_map(seed, seed_to_soil)
      fertilizer = find_in_map(soil, soil_to_fertilizer)
      water = find_in_map(fertilizer, fertilizer_to_water)
      light = find_in_map(water, water_to_light)
      temperature = find_in_map(light, light_to_temperature)
      humidity = find_in_map(temperature, temperature_to_humidity)
      location = find_in_map(humidity, humidity_to_location)
      locations.append(location)
    print("Part One:", min(locations))
    file.seek(0, SEEK_SET)
    print("Part Two:", part2(file.read()))
