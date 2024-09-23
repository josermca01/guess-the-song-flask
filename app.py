from flask import Flask, jsonify
import python  # Import your Python script
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

url_front_local = os.getenv("URL_FRONT_LOCAL")
url_front_remote = os.getenv("URL_FRONT_REMOTE")

app = Flask(__name__)
cors = CORS(app, resources={r"/get_playlist/*": {"origins": [url_front_local,url_front_remote]}})


@app.route('/get_playlist/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    text = python.main(playlist_id)
    response = jsonify(text)
    return response

if __name__ == '__main__':
    app.run(debug=True)