import json
import os

REGOLITH_PROJECT_ROOT = os.path.abspath(
  os.path.join(os.getcwd(), '../..')
)

""" Return regolith 'config.json' data. """
def get_regolith_config():
  CONFIG_JSON = os.path.abspath(
    os.path.join(REGOLITH_PROJECT_ROOT, 'config.json')
  )

  with open(CONFIG_JSON, 'r') as config_file:
    data = json.load(config_file)
    return data

def get_profile(name: str):
  profiles = get_regolith_config()['regolith']['profiles']

  if name in profiles:
    return profiles[name]
  else:
    return profiles['default']


def create_data_folder():
  dataPath = get_regolith_config()['regolith']['dataPath']

  DATA_FOLDER = os.path.abspath(
    os.path.join(REGOLITH_PROJECT_ROOT, dataPath, 'level')
  )

  if(not os.path.exists(DATA_FOLDER)):
    os.makedirs(DATA_FOLDER)


""" Return True if a profile is a specific target type. """
def is_target(profile: str, target: str) -> bool:
  return True if profile['export']['target'] == target else False
