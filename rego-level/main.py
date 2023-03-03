from utils import Regolevel

# Execute filter actions
def main():
  Regolevel.create_level_dir()
  Regolevel.copy_level()

if __name__ == '__main__':
  main()
