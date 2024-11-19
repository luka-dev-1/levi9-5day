from models import PlayerNickname
from config import redis_client

def player_create(nickname: PlayerNickname):
    """ Create a new player with the given nickname. """
    try:
        player = PlayerNickname(nickname=nickname)
        redis_client.hset("players", player.id, player)
        return 200, player
    except Exception as e:
        return 400, str(e)