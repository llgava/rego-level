import os
import uuid
from core.configuration import Configuration

BP_MANIFEST = os.path.join('BP', 'manifest.json')
RP_MANIFEST = os.path.join('RP', 'manifest.json')

BP_UUID = uuid.uuid4()
RP_UUID = uuid.uuid4()

# Execute filter actions
def main():
  print(Configuration.getTarget())
  """ print(Configuration.getName())
  print(Configuration.getDescription())
  print(Configuration.getVersion())
  print(Configuration.getBaseGameVersion()) """

if __name__ == '__main__':
  main()
