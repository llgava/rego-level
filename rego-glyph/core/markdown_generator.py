from tomark import Tomark
from core.image_properties import Glyph_E1
from core.models import *

def generate_markdown_file(save_to: str):
  """
    Generate a new Markdown file with glyph_E1 values.

    Args:
        save_to (str): The path to save the markdown file.
        glyph_E1 (str): The path to glyph_E1.png
  """
  print("Generating GLYPH_E1.md file...")

  glyphs = Glyph_E1.get_contents()
  glyph_table = Tomark.table(glyphs) # type: ignore

  with open(save_to, "w") as md_file:
    md_file.write(MARKDOWN_START)
    md_file.write(glyph_table)
    md_file.write(MARKDOWN_END)

  print(f"GLYPH_E1.md generated!")
