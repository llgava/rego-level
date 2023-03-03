import json
import os

REGOLITH_PROJECT_ROOT = os.path.abspath(
  os.path.join(os.getcwd(), '../..')
)

def get_config():
  CONFIG_JSON = os.path.abspath(
    os.path.join(REGOLITH_PROJECT_ROOT, 'config.json')
  )

  with open(CONFIG_JSON, 'r') as config_file:
    data = json.load(config_file)
    return data

def get_profile(name: str):
  profiles = get_config()['regolith']['profiles']

  if name in profiles:
    return profiles[name]
  else:
    return profiles['default']

def get_filters_from(profile: str):
  return get_config()['regolith']['profiles'][profile]['filters']
