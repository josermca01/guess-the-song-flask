from flask import Flask, jsonify,request
import python  # Import your Python script
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

url_front_local = os.getenv("URL_FRONT_LOCAL")
url_front_remote = os.getenv("URL_FRONT_REMOTE")

app = Flask(__name__)
cors = CORS(app, resources={r"/get_playlist/*": {"origins": [url_front_local,url_front_remote]}})
cors = CORS(app, resources={r"/search/*": {"origins": [url_front_local,url_front_remote]}})


@app.route("/")
def hello_world():
    return """
    <p>API Guess The Song</p>
    <p>Route to request a playlist at /get_playlist?playlist_id=theplaylistid</p>
    <p>Route to search for a playlist /search?query=playlistname</p>
    """

@app.route('/get_playlist', methods=['GET'])
def get_playlist():
    playlist_id = request.args.get('playlist_id',default=5206929684,type=int)
    text = python.get_playlist_tracks_by_id(playlist_id)
    response = jsonify(text)
    return response

@app.route('/search', methods=['GET'])
def search_playlist_id():
    query = request.args.get('query',default="Riot Games Worlds",type=str)
    text = python.search_playlist(query)
    response = jsonify(text)
    return response


if __name__ == '__main__':
    app.run(debug=True)