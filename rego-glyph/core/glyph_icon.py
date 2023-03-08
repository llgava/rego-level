from core.hex import *

class GlyphIcon:
  def __init__(self, code: str, preview: str, position: tuple[int, int]):
    self.hex = "0xE1" + code
    self.unicode = "U+E1" + code
    self.preview = preview
    self.position = position

  def to_dict(self):
    return {
      "hex": self.hex,
      "unicode": self.unicode,
      "preview": self.preview,
      "position": self.position
    }
