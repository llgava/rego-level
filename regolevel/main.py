import utils.RegolithConfig as RegolithConfig
import utils.BedrockPaths as BedrockPaths

def main():
  print('regolevel running...')
  profile = RegolithConfig.get_profile('build')

  GAME_PATH = BedrockPaths.get_game_path()
  BedrockPaths.get_worlds(GAME_PATH)

if __name__ == '__main__':
  main()
