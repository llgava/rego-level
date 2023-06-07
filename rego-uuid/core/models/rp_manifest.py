RP_MANIFEST = '''{
  "format_version": 2,
  "header": {
    "name": "$pack_name",
    "description": "$pack_description",
    "uuid": "$bp_uuid",
    "version": $pack_version,
    "min_engine_version": $game_version
  },

  "modules": [
    {
      "type": "resources",
      "uuid": "$random_uuid",
      "version": [1, 0, 0]
    }
  ]
}'''
