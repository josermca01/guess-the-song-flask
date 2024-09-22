from flask import Flask, jsonify
import python  # Import your Python script

app = Flask(__name__)

@app.route('/get_playlist/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    text = python.main(playlist_id)
    response = jsonify(text)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(debug=True)