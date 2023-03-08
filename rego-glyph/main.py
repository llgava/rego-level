import os
import core.image_properties as ImageProps

GLYPH_E1 = os.path.join('RP', 'font', 'glyph_E1.png')

# Execute filter actions
def main():
  ImageProps.getGlyphAreas(GLYPH_E1)

if __name__ == '__main__':
  main()
