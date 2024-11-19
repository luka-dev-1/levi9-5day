from models import PlayerNickname, Player
from config import redis_client

def player_create(nickname: PlayerNickname):
    """ Create a new player with the given nickname. """
    try:
        exists = redis_client.hexists("players", nickname)
        if exists:
            return 400, "Player already exists"
        
        player = Player(nickname=nickname)
        redis_client.hset("players", player.nickname, player)
        return 200, player
    except Exception as e:
        return 400, str(e)
    
def player_get(id: int):
    """ Get a player by their id. """
    try:
        player = redis_client.hget("players", id)
        if not player:
            return 404, "Player not found"
        return 200, player
    except Exception as e:
        return 400, str(e)