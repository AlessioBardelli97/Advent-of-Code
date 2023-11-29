from argparse import ArgumentParser
from pathlib import Path


if __name__ == "__main__":
    parser = ArgumentParser(prog="aoc2022")
    parser.add_argument("-d", "--day", required=True, type=int, choices=range(1, 26), help="Run code for Day of Advent of Code 2022")
    parser.add_argument("-r", "--res", help="Pass an input file to Day's code")

    args = parser.parse_args()

    code = Path(".") / f"Day{args.day}" / "src" / "main.py"

    if args.res:
        input_file = Path(".") / f"Day{args.day}" / "res" / args.res
    else:
        input_file = None

    if code.exists():
        with code.open() as file:
            print("Day", args.day)
            exec(file.read(), {"__name__": "__aoc2022__"}, {"input_file": input_file})
