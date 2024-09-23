import requests
import random

def get_playlist_by_id(playlist_id):
    # Step 1: Retrieve the tracks in the playlist
    NUMGAMES = 3
    NUMSONGS = 4
    TAM = 70
    url = f"https://api.deezer.com/playlist/{playlist_id}/tracks?limit={TAM}"
    response = requests.get(url)
    playlist_tracks = response.json()["data"]

    games = []
    answers = []

    # Step 2: For the every game, build an gameObject
    for _ in range(0,NUMGAMES):
        previews=[]
        tracks=[]
        
        # Step 3: Fill the track list with random songs from the Playlist
        while(len(tracks)<NUMSONGS):
            diff = NUMSONGS-len(tracks)
            random_tracks = random.choices(playlist_tracks,k=diff)
            # Step 3.1: Retrieve information for each track
            for track in random_tracks:
                new_track = {}
                new_track["title"] = track["title"]
                new_track["album"] = track["album"]["title"]
                new_track["cover"] = track["album"]["cover_medium"]
                new_track["artist"] = track["artist"]["name"]

                # Step 3.2: Save track if not repeated and store it preview separately for later
                if(track["preview"] !="" and not(track["preview"] in previews)):
                    previews.append(track["preview"])
                    tracks.append(new_track)

        # Step 4: Select a random preview that was not yet selected
        selected = False
        while(not selected):
            selected_preview = random.choice(previews)
            if(not selected_preview in answers):
                answers.append(selected_preview)
                selected = True

        # Step 5: Build the game object
        game = {}
        game["answer"] = previews.index(selected_preview) # INT - The index of the tracks list for that game
        game["preview"] = selected_preview # STR - The URL for the music preview source 
        game["tracks"] = tracks # LIST - All the tracks for that game
        
        games.append(game)

    return games

def search_playlist(query):
    url = f"https://api.deezer.com/search/playlist?q={query}"
    response = requests.get(url)
    playlists_query = response.json()["data"]

    playlists_infos=[]

    for playlist in playlists_query:
        new_playlist={}
        new_playlist["title"]=playlist["title"]
        new_playlist["id"]=playlist["id"]
        new_playlist["cover"]=playlist["picture_medium"]
        playlists_infos.append(new_playlist)

    print(playlists_infos)
    return playlists_infos
