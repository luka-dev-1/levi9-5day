import uuid
import json

class Player:
    def __init__(self, nickname, id=uuid.uuid4().hex, wins=0, losses=0, elo=0, hours_played=0, team=None, rating_adjustment=None):
        self.id = id
        self.nickname = nickname
        self.wins = wins
        self.losses = losses
        self.elo = elo
        self.hours_played = hours_played
        self.team = team
        self.rating_adjustment = rating_adjustment

    def __repr__(self):
        return (f"Player(id={self.id}, nickname={self.nickname}, wins={self.wins}, "
                f"losses={self.losses}, elo={self.elo}, hours_played={self.hours_played}, "
                f"team={self.team}, rating_adjustment={self.rating_adjustment})")

    def to_dict(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'wins': self.wins,
            'losses': self.losses,
            'elo': self.elo,
            'hours_played': self.hours_played,
            'team': self.team,
            'rating_adjustment': self.rating_adjustment
        }

    def to_json(self):
        return json.dumps(self.to_dict())