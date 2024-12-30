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
```jsonc
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
          Generates a simple HTML or JSON files listing all encrypted content with original values.
          This option is only for development purpose!

          Possible options:
            - true = Generates an HTML file (enderchest_webview.html) and JSON file (enderchest.json) with encrypted content.
            - false = Nothing will be generated. (Default option)
            - "html" = Generates ONLY the HTML file (enderchest_webview.html) with encrypted content.
            - "json" = Generates ONLY the JSON file (enderchest.json) with encrypted content.
        */
        "writeRelatory": true
      }
    }
  ]
}
```

## How an encrypted data looks like?

```jsonc
{
  "_id": "0a1b-2c3d",
  "filePath": "BP/items/my_custom_item.item.json",
  "encryptedFilePath": "BP/items/0a1b-2c3d.json",
  "data": [

    // A list of all encrypted content on this file.
    {
      "type": "IDENTIFIER",
      "hash": "4d899196dc6c9a140d36f05844f3fe67",
      "original": "my_custom:item_identifier",
      "encrypted": "4d899196dc6c9a14:0d36f05844f3fe67"
    }
  ]
}
```