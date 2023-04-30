import os
import time
import core.markdown_generator as MarkdownGenerator

SAVE_PATH = os.path.join('GLYPH_E1.md')

# Execute filter actions
def main():
  MarkdownGenerator.generate_markdown_file(SAVE_PATH)
  print(time.process_time())

if __name__ == '__main__':
  main()
