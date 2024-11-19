from flask import jsonify, make_response, request
from config.config import app
from services import players_service

@app.route('/players/create', methods=['POST'])
def create_player():
    body = request.get_json()
    if body.get('nickname') is None:
        return "Nickname is required", 400
    
    res, code = players_service.player_create(body['nickname'])
    if code >= 400:
        return res, code
    
    return make_response(res, code)

@app.route('/players/<id>', methods=['GET'])
def get_player(id: int):
    return players_service.player_get(id)