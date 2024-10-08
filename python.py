import requests
import random

urlplaylist = "https://api.deezer.com/playlist/"

def jsondata(url):
    response = requests.get(url)
    return response.json()


def get_playlist_by_id(playlist_id):
    url = urlplaylist+f"{playlist_id}"
    playlist_data = jsondata(url)
    playlist=[]

    new_playlist={}
    new_playlist["title"]=playlist_data["title"]
    new_playlist["id"]=playlist_data["id"]
    new_playlist["cover"]=playlist_data["picture_medium"]
    playlist.append(new_playlist)

    return playlist

def get_playlist_tracks_by_id(playlist_id):
    # Step 1: Retrieve the tracks in the playlist
    NUMGAMES = 3
    NUMSONGS = 4
    TAM = 70
    url = urlplaylist+f"{playlist_id}/tracks?limit={TAM}"
    playlist_tracks = jsondata(url)["data"]

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
    if(query.isnumeric()):
        return get_playlist_by_id(int(query))
    url = f"https://api.deezer.com/search/playlist?q={query}&limit=15"
    playlists_query = jsondata(url)["data"]

    playlists_infos=[]

    for playlist in playlists_query:
        new_playlist={}
        new_playlist["title"]=playlist["title"]
        new_playlist["id"]=playlist["id"]
        new_playlist["cover"]=playlist["picture_medium"]
        playlists_infos.append(new_playlist)

    return playlists_infos
