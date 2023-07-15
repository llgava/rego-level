import os
import sys
import subprocess

from utils.regolith import *

THIS_FILE_PATH = os.path.realpath(__file__)
CSHARP_COMPILER_PATH = os.path.dirname(THIS_FILE_PATH)
PROJECT_ROOT = os.path.abspath(os.path.join(CSHARP_COMPILER_PATH, '..', '..', '..', '..'))
PROJECT_CONFIGURATION = os.path.join(PROJECT_ROOT, "config.json")

def main():
  print("Compiling C# filters...")

  Regolith.build_csharp_filters(PROJECT_ROOT, PROJECT_CONFIGURATION)

if __name__ == '__main__':
  main()
