from core.models.rp_manifest import RP_MANIFEST
from core.manifest import Manifest

class ResourcePackManifest(Manifest):
  uuid = None
  rp_uuid = None

  def __init__(self, path: str, uuid: str) -> None:
    super().__init__(path, RP_MANIFEST)
    self.uuid = uuid
    self.updateModel()

  def updateModel(self):
    self.model = self.model \
      .replace('$rp_uuid', self.uuid)
