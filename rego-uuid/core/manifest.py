import os
import json
import json5
from uuid import uuid4
from pathlib import Path
from core.configuration import Configuration

class Manifest:
  path = None
  name = Configuration.getName()
  description = Configuration.getDescription()
  version = str(Configuration.getVersion())
  base_game_version = str(Configuration.getBaseGameVersion())
  model = None

  def __init__(self, path: str, model: str) -> None:
    self.path = path
    self.model = self.__buildModel(model)

  def __buildModel(self, model: str):
    return model \
      .replace('$pack_name', self.name) \
      .replace('$pack_description', self.description) \
      .replace('$pack_version', self.version) \
      .replace('$game_version', self.base_game_version) \
      .replace('$random_uuid', str(uuid4()))

  def build(self):
    if (os.path.exists(self.path)):
      os.remove(self.path)

    PATH = Path(self.path)
    manifestJSON = PATH.parent.resolve()
    os.makedirs(manifestJSON, exist_ok=True)

    with open(PATH, 'w') as file:
      initial_data = json5.loads(self.model)
      json.dump(initial_data, file, indent=2)

    return


  def update(self):
    print("SHOULD UPDATE!")
