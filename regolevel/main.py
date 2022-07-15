import utils.RegolithConfig as RegolithConfig
import utils.BedrockPaths as BedrockPaths

def main():
  print('Running regolevel...') # Should be removed in the future
  profile = RegolithConfig.get_profile('build')

  # Setup filter
  #RegolithConfig.create_data_folder()

  # Execute filter actions
  GAME_PATH = BedrockPaths.get_game_path()
  BedrockPaths.get_worlds(GAME_PATH)

if __name__ == '__main__':
  main()
