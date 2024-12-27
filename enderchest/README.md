# enderchest
Encrypt your Minecraft code with AES symmetric algorithm.

> [!WARNING]
> **Not recommended for Add-Ons development!**
> 
> **Why?** Since Add-Ons are like java mods and you want give more liberty for the player be able to do what they want with your product, why limit they to summon custom entities, setblock custom blocks etc...?
> 
> This filter is only recommended for IP products or other things like adventure maps.

## Instalation
```sh
regolith install github.com/llgava/regolith-filters/enderchest
```

## Configuration
```json
{
  "filters": [
    {
      "filter": "enderchest",
      "settings": {
        "keySize": 128, /* Valid values are: 128, 192 or 256. Default: 192. */
        "secretKey": "my_beautiful_key", /* Should correspond to the key size! For example 128 bits = 16 characters. */

        /*
          Array of files that should be ignored. Vanilla files and Manifests are already included in built-in.
          You can also use glob here to define a entire directory.
        */
        "ignore": [],

        /*
          Generates a simple HTML listing all encrypted content with original values and directories.
          This option is only for development purpose!
        */
        "writeRelatory": true
      }
    }
  ]
}
```
