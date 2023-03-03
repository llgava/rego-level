import os
import json5
from glob import glob

import utils.file_manager as FileManager

def remove_texture_atlas(path: str):
  """
    Removes Aseprite Texture Atlas configurations.
    This function only search files on specified path.
  """
  json_files = glob(root_dir=path, pathname="**/*.json", recursive=True)

  for file in json_files:
    full_path = os.path.join(path, file)
    name = os.path.basename(full_path).split("/")[-1]

    if (is_aseprite_texture_atlas(full_path)):
      FileManager.delete_file(full_path)
      print("Aseprite Texture Atlas: " + name + " successfully removed.")

def is_aseprite_texture_atlas(path: str) -> bool:
  json_file = open(path, 'r')
  data = json5.loads(json_file.read())

  if not ("meta" in data): return False
  if not ("app" in data["meta"]): return False

  return data["meta"]["app"] == "https://www.aseprite.org/"

def remove_files_with_ext(extensions: list):
  """
    Removes files with specified extensions.
  """
  files = glob(root_dir=".", pathname="**/*.*", recursive=True)

  for file in files:
    path, ext = os.path.splitext(file)

    if (ext == ".json"): continue

    if (ext in extensions):
      full_path = path + ext
      name = os.path.basename(full_path).split("/")[-1]

      FileManager.delete_file(full_path)
      print("Extension not allowed/required: " + name + " successfully removed.")
