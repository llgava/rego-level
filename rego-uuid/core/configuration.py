import sys
import json
from default_config import DEFAULT_CONFIGURATION

ALLOWED_TARGETS = ['world', 'development', 'dev']

class Configuration:
  LOG_DEFAULT_SETTINGS = False

  @staticmethod
  def getTarget():
    value = Configuration.__getSetting('target').lower()

    if not (value in ALLOWED_TARGETS):
      print("Target not allowed, please use one of the targets bellow:")
      print(" • world\n • development\n • dev")
      print(f"Using default target. ({DEFAULT_CONFIGURATION['target']})")
      return DEFAULT_CONFIGURATION['target']

    return value

  @staticmethod
  def getName():
    return Configuration.__getSetting('name')

  @staticmethod
  def getDescription():
    return Configuration.__getSetting('description')

  @staticmethod
  def getVersion():
    version = Configuration.__getStringAsList(
      Configuration.__getSetting('version')
    )

    if (len(version) > 3 or len(version) < 3):
      print("Version not allowed, please use a matrix versions like '1.0.0'.")
      print(f"Using default version. ({DEFAULT_CONFIGURATION['version']})")
      return DEFAULT_CONFIGURATION['version']

    return version

  @staticmethod
  def getBaseGameVersion():
    version = Configuration.__getStringAsList(
      Configuration.__getSetting('base_game_version')
    )

    if (len(version) > 3 or len(version) < 3):
      print("Base Game Version not allowed, please use a matrix versions like '1.20.0' or '1.20.10'.")
      print(f"Using default base_game_version. ({DEFAULT_CONFIGURATION['base_game_version']})")
      return DEFAULT_CONFIGURATION['base_game_version']

    return version

  @staticmethod
  def __getSetting(value: str):
    try:
      settings = json.loads(sys.argv[1])

      try:
        settings = settings[value]
      except IndexError:
        print(f"No {value} setting found! Using default {value} setting.")
        settings = DEFAULT_CONFIGURATION[value]

    except IndexError:
      if not (Configuration.LOG_DEFAULT_SETTINGS):
        print("No settings found! Using default settings.")

      Configuration.LOG_DEFAULT_SETTINGS = True

      settings = DEFAULT_CONFIGURATION[value]


    return settings

  @staticmethod
  def __getStringAsList(value: str):
    return [int(i) for i in value.split(".")]
