from flask import Flask, jsonify,request
import python  # Import your Python script
from flask_cors import CORS
from dotenv import load_dotenv
import os
from flasgger import Swagger,swag_from
import specs_swagger

load_dotenv()

url_front = os.getenv("URL_FRONT")

app = Flask(__name__)
swagger = Swagger(app,config=specs_swagger.swagger_config)
cors = CORS(app, resources={r"/get_playlist/*": {"origins": url_front}})
cors = CORS(app, resources={r"/search/*": {"origins": url_front}})
 
@app.route('/get_playlist', methods=['GET'])
@swag_from(specs_swagger.specs_game)
def get_playlist():
    playlist_id = request.args.get('playlist_id',default=5206929684,type=int)
    text = python.get_playlist_tracks_by_id(playlist_id)
    response = jsonify(text)
    return response

@app.route('/search', methods=['GET'])
@swag_from(specs_swagger.specs_query)
def search_playlist_id():
    query = request.args.get('query',default="Riot Games Worlds",type=str)
    text = python.search_playlist(query)
    response = jsonify(text)
    return response


if __name__ == '__main__':
    app.run(debug=True)