import os
import platform

APPDATA = os.getenv('LOCALAPPDATA')
WORLDS = []

def get_game_path() -> str:
  if(platform.system() != 'Windows'):
    raise AssertionError('Unsupported operating system: ' + platform.system())

  return os.path.join(APPDATA, 'Packages', 'Microsoft.MinecraftUWP_8wekyb3d8bbwe', 'LocalState', 'games', 'com.mojang')

def get_worlds(game_path: str):
  for (root, dirs, files) in os.walk(f"{game_path}/minecraftWorlds"):
    for dir in dirs:
      print(dir)

""" def is_wsl() -> bool:
  return 'microsoft-standard' in platform.uname().release """
