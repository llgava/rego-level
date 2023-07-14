import os
import sys
import subprocess

def main():
  this_path = os.path.realpath(__file__)
  filters_dir = os.path.dirname(this_path)
  test_dir = os.path.join('..', '..', '..', filters_dir)

  print("Compiling C# filters...")
  print("")

  print("THIS_PATH", this_path)
  print("FILTERS_DIR", filters_dir)
  print("TEST_DIR", test_dir)

if __name__ == '__main__':
  main()
