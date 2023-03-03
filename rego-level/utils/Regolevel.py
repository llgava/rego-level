import ast
import os
import shutil
import sys
from utils import Bedrock

def get_setting(arg: str):
  raw_arguments = sys.argv[1]
  args = ast.literal_eval(raw_arguments)

  return args[arg]

def create_level_dir():
  LEVEL_PATH = os.path.abspath(
    os.path.join(os.getcwd(), '../..', get_setting('levelPath'))
  )

  if(not os.path.exists(LEVEL_PATH)):
    os.mkdir(LEVEL_PATH)

def copy_level():
  LEVEL_PATH = os.path.abspath(
    os.path.join(os.getcwd(), '../..', get_setting('levelPath'))
  )

  if(not Bedrock.get_world(get_setting('worldName')) is None):

    for (root, dirs, _files) in os.walk(LEVEL_PATH):
      file_destination = Bedrock.get_world(get_setting('worldName'))['path'] + root.replace(LEVEL_PATH, '')

      if('db' in dirs):
        shutil.rmtree(os.path.join(file_destination, 'db'), ignore_errors=True)

      shutil.copytree(root, file_destination, dirs_exist_ok=True)
  else:
    print('Unable to find the world', get_setting('worldName'))
