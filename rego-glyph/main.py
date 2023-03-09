import os
import core.markdown_generator as MarkdownGenerator

GLYPH_E1 = os.path.join('example', 'resource_pack', 'font', 'glyph_E1.png')
SAVE_PATH = os.path.join('GLYPH_E1.md')

# Execute filter actions
def main():
  MarkdownGenerator.generate_markdown_file(SAVE_PATH)

if __name__ == '__main__':
  main()
