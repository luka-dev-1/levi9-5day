from config.config import app
from models import PlayerNickname
from services import players_service

@app.route('/players/create', methods=['POST'])
def create_player(request):
    body = request.get_json()
    return players_service.player_create(body)

@app.route('/players/<id>', methods=['GET'])
def get_player(id: int):
    return players_service.player_get(id)