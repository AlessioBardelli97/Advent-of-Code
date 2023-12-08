from functools import reduce
from sys import argv
from math import floor
from math import lcm


class Monkey:
    def __init__(self, items: list[int], operation: list[str], test: int, if_true: int, if_false: int) -> None:
        self.items = list(items)
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspects_items_time = 0
    def throw(self, item: int):
        self.items.append(item)
    def turn_part_one(self, monkeys: list["Monkey"]):
        for item in self.items:
            self.inspects_items_time += 1
            if self.operation[0] == "+":
                if self.operation[1] == "old":
                    worry_level = item + item
                else:
                    worry_level = item + int(self.operation[1])
            else:
                if self.operation[1] == "old":
                    worry_level = item * item
                else:
                    worry_level = item * int(self.operation[1])
            worry_level = floor(worry_level / 3)
            if worry_level % self.test == 0:
                monkeys[self.if_true].throw(worry_level)
            else:
                monkeys[self.if_false].throw(worry_level)
        self.items.clear()
    def turn_part_two(self, monkeys: list["Monkey"], least_common_multiple: int):
        for item in self.items:
            self.inspects_items_time += 1
            if self.operation[0] == "+":
                if self.operation[1] == "old":
                    worry_level = item + item
                else:
                    worry_level = item + int(self.operation[1])
            else:
                if self.operation[1] == "old":
                    worry_level = item * item
                else:
                    worry_level = item * int(self.operation[1])
            worry_level %= least_common_multiple
            if worry_level % self.test == 0:
                monkeys[self.if_true].throw(worry_level)
            else:
                monkeys[self.if_false].throw(worry_level)
        self.items.clear()
    def __repr__(self) -> str:
        return f"Monkey({self.inspects_items_time=})"


def parseNotes(notes: str) -> list[Monkey]:
    result: list[Monkey] = []
    notes_list = notes.split("\n")
    for idx_line in range(0, len(notes_list), 7):
        items = list(map(int, notes_list[idx_line+1][18:].split(", ")))
        operation = notes_list[idx_line+2][23:].split(" ")
        test = int(notes_list[idx_line+3][21:])
        if_true = int(notes_list[idx_line+4][29:])
        if_false = int(notes_list[idx_line+5][30:])
        result.append(Monkey(items, operation, test, if_true, if_false))
    return result


def mul(iterable: list[int]) -> int:
    return reduce(lambda val, tot: tot * val, iterable, 1)


def monkey_business(monkeys: list["Monkey"]) -> int:
    return mul(sorted(map(lambda m: m.inspects_items_time, monkeys))[-2:])


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        notes = file.read()
        monkeys = parseNotes(notes)
        for round in range(20):
            for monkey in monkeys:
                monkey.turn_part_one(monkeys)
        print("Part One:", monkey_business(monkeys))
        monkeys = parseNotes(notes)
        least_common_multiple = lcm(*[m.test for m in monkeys])
        for round in range(10_000):
            for monkey in monkeys:
                monkey.turn_part_two(monkeys, least_common_multiple)
        print("Part Two:", monkey_business(monkeys))
