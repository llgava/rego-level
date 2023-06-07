BP_MANIFEST = '''{
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
      "type": "data",
      "uuid": "$random_uuid",
      "version": [1, 0, 0]
    }
  ],

  "dependencies": [
    {
      "uuid": "$rp_uuid",
      "version": $pack_version
    }
  ]
}'''
