# rego-level
Remove the old world files to new ones on every build. (Need game restart every time)

## Instalation
```sh
regolith install github.com/llgava/regolith-filters/rego-level
```

## Configuration
```json
{
  "filters": [
    {
      "filter": "rego-level",
      "settings": {
        "levelPath": "./packs/level",
        "worldName": "Spellcraft"
      }
    }
  ]
}
```
