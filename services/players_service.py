from models import Player
from config import redis_client


def player_create(nickname: str):
    """ Create a new player with the given nickname. """
    try:
        exists = redis_client.hexists("players", nickname)
        if exists:
            return "Player already exists", 400
        
        player = Player(nickname=nickname)
        redis_client.hset("players", player.nickname, player.to_json())
        return player.to_json(), 201
    except Exception as e:
        return str(e), 400
    
def player_get(id: int):
    """ Get a player by their id. """
    try:
        player = redis_client.hget("players", id)
        if not player:
            return 404, "Player not found"
        return 200, player
    except Exception as e:
        return 400, str(e)