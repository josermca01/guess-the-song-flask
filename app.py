from flask import Flask, jsonify
import python  # Import your Python script
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/get_playlist/*": {"origins": "http://localhost:5173/*"}})


@app.route('/get_playlist/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    text = python.main(playlist_id)
    response = jsonify(text)
    return response

if __name__ == '__main__':
    app.run(debug=True)