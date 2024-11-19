from config.config import app
from models import PlayerNickname
from services import players_service

@app.route('/players/create', methods=['POST'])
def create_player(nickname: PlayerNickname):
    return players_service.player_create(nickname)