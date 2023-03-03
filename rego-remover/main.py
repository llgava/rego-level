import os
import remover as RemoveManager

TEXTURES_FOLDER = os.path.join('RP', 'textures')

# Execute filter actions
def main():
  RemoveManager.remove_texture_atlas(TEXTURES_FOLDER)
  RemoveManager.remove_files_with_ext([
    ".ase", ".bbmodel", ".DS_Store",
    ".txt", ".js", ".py", ".ts"
  ])

if __name__ == '__main__':
  main()
