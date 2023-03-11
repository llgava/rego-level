import os
import json
import json5
from glob import glob

import utils.file_manager as FileManager

def remove_aseprite_flipbooks(path: str):
  """ Removes Aseprite JSON Animations from invalid paths. """
  print("Removing Aseprite Flip book on invalid paths...")
  json_files = glob(root_dir=path, pathname="**/*.json", recursive=True)

  for file in json_files:
    full_path = os.path.join(path, file)

    if (_is_invalid_aseprite_flipbook(full_path)):
      FileManager.delete_file(full_path)

def _is_invalid_aseprite_flipbook(path: str) -> bool:
  if ("textures/ui" in path): return False

  json_file = open(path, 'r')
  data = json5.loads(json_file.read())

  if not ("meta" in data): return False
  if not ("app" in data["meta"]): return False

  return data["meta"]["app"] == "https://www.aseprite.org/"

def remove_geckolib_artifacts(path: str) -> None:
  """ Removes Geckolib animations objects. """
  print("Removing Geckolib animations artifacts...")
  json_files = glob(root_dir=path, pathname="**/*.json", recursive=True)

  for file in json_files:
    full_path = os.path.join(path, file)
    json_file = open(full_path, 'r')
    data = json5.loads(json_file.read())
    animations = data["animations"]

    if ("geckolib_format_version" in data):
      del data["geckolib_format_version"]

    for anim in list(animations):
      if (anim.endswith("_unbaked")):
        del animations[anim]

    with open(full_path, 'w') as anim_file:
      json.dump(data, anim_file, indent=2)

def remove_files_with_ext(extensions: list):
  """ Removes files with specified extensions. """
  print("Removing not allowed/required files...")
  files = glob(root_dir=".", pathname="**/*.*", recursive=True)

  for file in files:
    path, ext = os.path.splitext(file)

    if (ext == ".json"): continue

    if (ext in extensions):
      full_path = path + ext
      FileManager.delete_file(full_path)
