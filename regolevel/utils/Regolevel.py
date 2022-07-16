import ast
import os
import shutil
import sys
from utils import Bedrock

def get_setting(arg: str):
  raw_arguments = sys.argv[1]
  args = ast.literal_eval(raw_arguments)

  return args[arg]


def copy_level():
  LEVEL_PATH = os.path.abspath(
    os.path.join(os.getcwd(), '../..', get_setting('levelPath'))
  )

  for (root, _dirs, _files) in os.walk(LEVEL_PATH):
    file_destination = Bedrock.get_world(get_setting('worldName'))['path'] + root.replace(LEVEL_PATH, '')
    shutil.copytree(root, file_destination, dirs_exist_ok=True)
