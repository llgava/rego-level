from core.models.bp_manifest import BP_MANIFEST
from core.manifest import Manifest

class BehaviorPackManifest(Manifest):
  uuid = None
  rp_uuid = None

  def __init__(self, path: str, uuid: str, rp_uuid: str) -> None:
    super().__init__(path, BP_MANIFEST)
    self.uuid = uuid
    self.rp_uuid = rp_uuid

    self.updateModel()

  def updateModel(self):
    self.model = self.model \
      .replace('$bp_uuid', self.uuid) \
      .replace('$rp_uuid', self.rp_uuid)
