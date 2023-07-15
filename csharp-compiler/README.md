# csharp-compiler
Automatically build a .dll file for all C# local filters on the project.

## Instalation
```sh
regolith install github.com/llgava/regolith-filters/csharp-compiler
```

## Configuration
Note that your C# filter should only be called **after** csharp-compiler has been run.

```json
{
  "filters": [
    { "filter": "csharp-compiler" },
    { "filter": "my_csharp_local_filter" },
    { "filter": "other_csharp_local_filter" }
  ]
}
```

## Filter definition pattern
You also need to follow a pattern for your C# path. See the example bellow:

```json
...
"filterDefinitions": {
	"csharp-compiler": {
		"url": "github.com/llgava/regolith-filters",
		"version": "1.0.0"
	},
	"my_csharp_local_filter": {
		"path": "./YOUR_FILTER_PATH/Build/my_csharp_local_filter.dll",
		"runWith": "dotnet"
	},
	"other_csharp_local_filter": {
		"path": "./YOUR_FILTER_PATH/Build/other_csharp_local_filter.dll",
		"runWith": "dotnet"
	}
}
...
```

Basically the default for the path should be `./YOUR_FILTER_PATH/Build/YOUR_FILTER_NAME.dll`
