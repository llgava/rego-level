import os
import json
import subprocess

class Regolith:

  @staticmethod
  def build_csharp_filters(project_root: str, config: str):
    filters = Regolith.get_csharp_local_filters(config)

    for _filter in filters:
      name = _filter['name']
      path = _filter['path']
      parsed_path = path.replace(f"Build/{name}.dll", f"{name}.csproj")
      csproj_path = os.path.abspath(os.path.join(project_root, parsed_path))

      print(f" * Compiling {name} filter...\n")

      csproj_restore_cmd = f"dotnet build {csproj_path} /nologo /clp:NoSummary"
      subprocess.run(csproj_restore_cmd, shell=True)

      csproj_build_cmd = f"dotnet msbuild {csproj_path} /t:Rebuild /p:Configuration=Release /p:OutPutPath=./Build"
      subprocess.run(csproj_build_cmd, shell=True)
      print("")

  @staticmethod
  def get_csharp_local_filters(config: str) -> list:
    local_filters = []

    with open(config, 'r') as file:
      data = json.load(file)

      definitions = data['regolith']['filterDefinitions']

      for definition in definitions:
        if not ("path" in definitions[definition]): continue
        if not ("runWith" in definitions[definition]): continue
        if not (definitions[definition]["runWith"] == "dotnet"): continue

        local_filters.append({
          "name": definition,
          "path": definitions[definition]["path"],
          "runWith": "dotnet"
        })

    return local_filters
