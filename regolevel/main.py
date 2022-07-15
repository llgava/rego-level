import utils.RegolithConfig as RegolithConfig
import utils.BedrockPaths as BedrockPaths

def main():
  print('Running regolevel...') # Should be removed in the future
  profile = RegolithConfig.get_profile('build')

  # Setup filter
  #RegolithConfig.create_data_folder()

  # Execute filter actions
  worlds = BedrockPaths.get_worlds()
  print(worlds)

if __name__ == '__main__':
  main()
