from enum import Enum

class HexParser(Enum):
  A = 10
  B = 11
  C = 12
  D = 13
  E = 14
  F = 15

def parse(value: int):
  if (value >= 0 and value <= 9):
    return str(value)

  for item in HexParser:
    if item.value == value:
      return item.name

  return str(0)
