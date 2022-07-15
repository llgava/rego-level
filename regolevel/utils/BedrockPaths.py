import os
import platform

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

      with open(LEVELNAME_TXT, 'r') as levelname_file:
        WORLDS.append(
          {
            'name': levelname_file.readline(),
            'path': WORLD_FOLDER
          }
        )

  return WORLDS


""" def is_wsl() -> bool:
  return 'microsoft-standard' in platform.uname().release """
