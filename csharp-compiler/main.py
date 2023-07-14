import os
import sys
import subprocess

def main():
  this_path = os.path.realpath(__file__)
  filters_dir = os.path.dirname(this_path)

  parent_dir = os.path.dirname(path)
  project_dir = os.path.abspath(os.path.join(parent, '..', '..', '..'))

  print("Compiling C# filters...")
  print("")

  print("THIS_PATH", this_path)
  print("FILTERS_DIR", filters_dir)
  print("PARENT_DIR", parent_dir)
  print("PROJECT_DIR", project_dir)

if __name__ == '__main__':
  main()
