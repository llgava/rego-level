WORLD_MANIFEST = '''{
	"format_version": 2,
	"header": {
		"name": "pack.name",
		"description": "pack.description",
		"uuid": "$world_uuid",
		"version": $pack_version,
		"base_game_version": $game_version,
		"lock_template_options": true
	},

	"modules": [
		{
			"type": "world_template",
			"uuid": "$random_uuid",
			"version": [1, 0, 0]
		}
	]
}
'''
