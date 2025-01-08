from sys import argv
from enum import IntEnum
from functools import total_ordering
from collections import Counter


cardValue = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "T": 8, "J": 9, "Q": 10, "K": 11, "A": 12}
cardValue_with_joker = {"J": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "Q": 10, "K": 11, "A": 12}


class Type(IntEnum):
  High  = 1
  One   = 2
  Two   = 3
  Three = 4
  Full  = 5
  Four  = 6
  Five  = 7


@total_ordering
class Hand:
  def __init__(self, cards: str, bid: str, with_joker: bool=False) -> None:
    self.cards = cards
    cardsDict = Counter(cards)
    self.bid = int(bid)
    self.with_joker = with_joker
    values = cardsDict.values()
    if len(values) == 1:
      self.type = Type.Five
    elif len(values) == 2:
      if any(x == 4 for x in values):
        if with_joker and "J" in cardsDict:
          self.type = Type.Five
        else:
          self.type = Type.Four
      elif any(x == 3 for x in values):
        if with_joker and "J" in cardsDict:
          self.type = Type.Five
        else:
          self.type = Type.Full
    elif len(values) == 3:
      if any(x == 3 for x in values):
        if with_joker and "J" in cardsDict:
          self.type = Type.Four
        else:
          self.type = Type.Three
      elif any(x == 2 for x in values):
        if with_joker and "J" in cardsDict:
          if cardsDict["J"] == 1:
            self.type = Type.Full
          else:
            self.type = Type.Four
        else:
          self.type = Type.Two
    elif len(values) == 4:
      if with_joker and "J" in cardsDict:
        self.type = Type.Three
      else:
        self.type = Type.One
    elif len(values) == 5:
      if with_joker and "J" in cardsDict:
        self.type = Type.One
      else:
        self.type = Type.High

  def __repr__(self) -> str:
    return f"Hand(cards={self.cards}, type={self.type.name}, bid={self.bid})"

  def __lt__(self, other: object) -> bool:
    if not isinstance(other, Hand):
      return False
    elif self.type == other.type:
      i = 0
      while self.cards[i] == other.cards[i]:
        i += 1
      if not self.with_joker:
        return cardValue[self.cards[i]] < cardValue[other.cards[i]]
      else:
        return cardValue_with_joker[self.cards[i]] < cardValue_with_joker[other.cards[i]]
    else:
      return self.type < other.type

  def __eq__(self, other: object) -> bool:
    if not isinstance(other, Hand):
      return False
    return self.cards == other.cards


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    hands: list[Hand] = []
    hands_with_joker: list[Hand] = []
    for line in file.readlines():
      cards, bid = line.split()
      hands.append(Hand(cards, bid))
      hands_with_joker.append(Hand(cards, bid, True))
    hands.sort()
    hands_with_joker.sort()
    print("Part One:", sum(rank * hand.bid for rank, hand in enumerate(hands, 1)))
    print("Part Two:", sum(rank * hand.bid for rank, hand in enumerate(hands_with_joker, 1)))
