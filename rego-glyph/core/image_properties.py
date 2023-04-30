import os
from PIL import Image
from core.glyph_content import GlyphContent
from core.hex import HexParser

class Glyph_E1:
  IMAGE_PATH = os.path.join('RP', 'font', 'glyph_E1.png')
  PREVIEW_PATH = os.path.join('.github', 'assets')

  @staticmethod
  def get_size() -> tuple[int, int]:
    """
      Args:
          glyph_E1 (str): The path to glyph_E1.png.

      Returns:
          tuple[int, int]: The size of glyph_E1.png
    """

    image = Image.open(Glyph_E1.IMAGE_PATH)
    width, height = image.size

    return (width, height)

  @staticmethod
  def get_content_size() -> tuple[int, int]:
    """
      Args:
          glyph_E1 (str): The path to glyph_E1.png.

      Returns:
          tuple[int, int]: The size of contents.
    """

    width, height = Glyph_E1.get_size()

    return (int(width / 16), int(height / 16))

  @staticmethod
  def get_contents() -> list[dict]:
    """
      Return a list of content on glyph_E1.png.\n
      Only contents with 5+ pixels are valid.

      Args:
          glyph_E1 (str): The path to glyph_E1.png.

      Returns:
          list[dict]: A list of glyph_E1.png content.
    """
    print(f"Collecting content from {Glyph_E1.IMAGE_PATH}...")

    valid_glyphs = []
    glyph_w, glyph_h = Glyph_E1.get_size()
    content_w, content_h = Glyph_E1.get_content_size()

    initial_pos = (0, 0, content_w, content_h)
    current_content_pos = initial_pos

    current_column = 0
    current_line = 0

    content_index = 0
    max_contents = int((glyph_w / content_w) * 16)

    while not (content_index == max_contents):
      if (current_column == (glyph_w / content_w)):
        current_column = 0
        current_line += 1
        current_content_pos = (
          initial_pos[0],
          current_content_pos[1] + content_h,
          initial_pos[2],
          current_content_pos[3] + content_h,
        )

      image = Image.open(Glyph_E1.IMAGE_PATH)
      cropped_image = image.crop(current_content_pos)

      current_content_pos = (
        current_content_pos[0] + content_w,
        current_content_pos[1],
        current_content_pos[2] + content_w,
        current_content_pos[3],
      )

      # Check if the cropped area is empty
      valid_pixels = []
      pixels = cropped_image.load()
      content_w, content_h = Glyph_E1.get_content_size()

      for x in range(content_w):

        for y in range(content_h):
          pixel = pixels[x, y] # type: ignore

          if (pixel == (0, 0, 0, 0)): continue

          valid_pixels.append(pixel)

      if (len(valid_pixels) >= 5):
        CODE = HexParser.parse(current_line) + HexParser.parse(current_column)
        IMAGE_MD = f"![preview_{content_index}](.github/assets/preview_{content_index}.png)"
        POS = (current_column, current_line)

        cropped_image_resized = cropped_image.resize((32, 32), Image.BOX)
        cropped_image_resized.save(f"{Glyph_E1.PREVIEW_PATH}/preview_{content_index}.png")

        valid_glyphs.append(
          GlyphContent(CODE, IMAGE_MD, POS)
            .to_dict()
        )

      current_column += 1
      content_index+=1

    print("Content collected!")
    return valid_glyphs
