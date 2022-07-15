import json
import os

def get_profile(name: str):
  CONFIG_JSON = os.path.join(os.getcwd(), 'config.json')

  with open(CONFIG_JSON, 'r') as config_file:
    data = json.load(config_file)
    profiles = data['regolith']['profiles']

    if(name in profiles):
      profile = profiles[name]
      return profile

""" Return True if a profile is a specific target type. """
def is_target(profile: str, target: str) -> bool:
  return True if profile['export']['target'] == target else False
