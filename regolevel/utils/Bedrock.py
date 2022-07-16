import os
import platform
import time
from utils import Regolevel

APPDATA = os.getenv('LOCALAPPDATA')

def get_game_path() -> str:
  if(platform.system() != 'Windows'):
    raise AssertionError('Unsupported operating system: ' + platform.system())

  return os.path.join(APPDATA, 'Packages', 'Microsoft.MinecraftUWP_8wekyb3d8bbwe', 'LocalState', 'games', 'com.mojang')

def get_worlds(game_path = get_game_path()):
  WORLDS = []

  for dir in os.listdir(f'{game_path}/minecraftWorlds'):
    WORLD_FOLDER = os.path.join(game_path, 'minecraftWorlds', dir)

    if(os.path.isdir(WORLD_FOLDER)):
      LEVELNAME_TXT = os.path.join(WORLD_FOLDER, 'levelname.txt')

      if(os.path.exists(LEVELNAME_TXT)):
        with open(LEVELNAME_TXT, 'r') as levelname_file:
          WORLDS.append(
            {
              'name': levelname_file.readline(),
              'path': WORLD_FOLDER,
              'last_modified': get_world_last_modified(WORLD_FOLDER)
            }
          )

  return WORLDS

def get_world(name: str):
  for world in get_worlds():
    if(world['name'] == name):
      return world

def get_world_last_modified(path: str):
  modification_time_stamp = os.path.getmtime(path)
  modification_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modification_time_stamp))

  return modification_time

""" Testing WSL compatibility on the future.
def is_wsl() -> bool:
  return 'microsoft-standard' in platform.uname().release """
