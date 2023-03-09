from core.hex import *

class GlyphContent:
  def __init__(self, code: str, preview: str, position: tuple[int, int]):
    self.hex = "0xE1" + code
    self.unicode = "U+E1" + code
    self.symbol = "&#" + HexParser.to_decimal(self.hex) + ";"
    self.preview = preview
    self.position = position

  def to_dict(self) -> dict:
    """
      Returns:
          dict: GlyphIcon as dict
    """

    return {
      "Hex": self.hex,
      "Unicode": self.unicode,
      "Symbol": self.symbol,
      "Preview": self.preview,
      "Position": self.position
    }
