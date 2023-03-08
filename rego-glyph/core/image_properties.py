from PIL import Image

def getImageSize(path: str):
  image = Image.open(path)
  w, h = image.size

  return (w, h)

def getAreaImageSize(path: str):
  w, h = getImageSize(path)

  return (int(w / 16), int(h / 16))

def getGlyphAreas(path: str):
  glyph_w, glyph_h = getImageSize(path)
  area_w, area_h = getAreaImageSize(path)

  initial_area = (0, 0, area_w, area_h)
  current_area_position = initial_area

  current_column = 0
  current_line = 0

  max_images = int((glyph_w / area_w) * 16)
  i = 0
  while not (i == max_images):
    if (current_column == (glyph_w / area_w)):
      current_column = 0
      current_line += 1
      current_area_position = (
        initial_area[0],
        current_area_position[1] + area_h,
        initial_area[2],
        current_area_position[3] + area_h,
      )

    image = Image.open(path)
    cropped_image = image.crop(current_area_position)

    current_area_position = (
      current_area_position[0] + area_w,
      current_area_position[1],
      current_area_position[2] + area_w,
      current_area_position[3],
    )

    # Check if the cropped area is empty
    valid_pixels = []
    pixels = cropped_image.load()
    area_w, area_h = getAreaImageSize(path)

    for x in range(area_w):
      for y in range(area_h):
        pixel = pixels[x, y]

        if (pixel == (0, 0, 0, 0)): continue

        valid_pixels.append(pixel)

    if (len(valid_pixels) >= 5):
      cropped_image_resized = cropped_image.resize((32, 32), Image.BOX)
      cropped_image_resized.save(f"test/gen/test_{i}.png")

    current_column += 1
    i+=1

  print("Collection finished.")
