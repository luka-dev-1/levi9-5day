from config.config import app
from models import PlayerNickname

@app.route('/players/create', methods=['POST'])
def create_player(nickname: PlayerNickname):
    return 