# rego-uuid
Setup every manifest uuid for your project.

Use this filter only for an setup of your project! It will overwrite existing manifests in the compile.

## Instalation
```sh
regolith install github.com/llgava/regolith-filters/rego-uuid
```

## Configuration
```json
{
  "filters": [
    {
      "filter": "rego-uuid",
      "settings": {
        "target": "dev",
        "name": "My Project Name",
        "description": "My Project Description.",
        "version": "1.0.0",
        "base_game_version": "1.20.0"
      }
    }
  ]
}
```

### Settings
If settings are not configured, default values will be used.

| Configuration    | Type    | Default | Description                                         |
|------------------|---------|---------|-----------------------------------------------------|
| target           | world, development or dev | dev    | Does nothing yet.         |
| name | string | pack.name    | The name of the project. |
| description | string | pack.description    | The description of the project. |
| version | string | 1.0.0    | The version of the project. |
| base_game_version | string | 1.20.0    | The minimum required version of Minecraft for the project. |
