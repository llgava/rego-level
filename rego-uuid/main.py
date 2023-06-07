import os
import sys
import json
from uuid import uuid4
from default_config import DEFAULT_CONFIGURATION
from core.configuration import Configuration
from core.behavior_pack import BehaviorPackManifest
from core.resource_pack import ResourcePackManifest

BP_MANIFEST = os.path.join('BP', 'manifest.json')
RP_MANIFEST = os.path.join('RP', 'manifest.json')

BP_UUID = str(uuid4())
RP_UUID = str(uuid4())

# Execute filter actions
def main():
  BehaviorPackManifest(BP_MANIFEST, BP_UUID, RP_UUID).build()
  ResourcePackManifest(RP_MANIFEST, RP_UUID).build()

if __name__ == '__main__':
  main()
