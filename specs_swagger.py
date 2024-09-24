specs_game = {
  "parameters": [
    {
      "name": "playlist_id",
      "in": "query",
      "type": "int",
      "default": 5206929684
    }
  ],
  "responses": {
    "200": {
      "description": "A list of 12 tracks of the playlist",
    }
  }
}
specs_query = {
    "parameters": [
    {
      "name": "query",
      "in": "query",
      "type": "string",
      "default": "Linkin Park"
    }
  ],
  "responses": {
    "200": {
      "description": "A list of playlists that have the requested name or the id",
    }
  }
}
swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/"
}