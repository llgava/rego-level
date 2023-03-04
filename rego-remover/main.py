import os
import core.remover as RemoveManager

TEXTURES_FOLDER = os.path.join('RP', 'textures')
ANIMATIONS_FOLDER = os.path.join('RP', 'animations')

# Execute filter actions
def main():
  RemoveManager.remove_texture_atlas(TEXTURES_FOLDER)
  RemoveManager.remove_geckolib_artifacts(ANIMATIONS_FOLDER)
  RemoveManager.remove_files_with_ext([
    ".ase", ".bbmodel", ".DS_Store"
  ])

if __name__ == '__main__':
  main()
