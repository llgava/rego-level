from enum import Enum

class HexParserEnum(Enum):
  A = 10
  B = 11
  C = 12
  D = 13
  E = 14
  F = 15

class HexParser:
  @staticmethod
  def parse(value: int) -> str:
    """
      Convert tens+ to hexadecimal values.

      Args:
          value (int): The number to convert in hexadecimal.
      Returns:
          str: The number converted in hexadecimal.
    """

    if (value >= 0 and value <= 9):
      return str(value)

    for item in HexParserEnum:
      if item.value == value:
        return item.name

    return str(0)

  @staticmethod
  def to_decimal(value: str) -> str:
    """
      Convert hexadecimal string into decimal string.

      Args:
          value (str): Hexadecimal string.
      Returns:
          str: The hexadecimal string converted into decimal string
    """

    return str(int(value, 16))
