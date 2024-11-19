from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_redis import FlaskRedis
import os

load_dotenv()

redis_config = {
    'host': os.getenv('REDIS_HOST', 'localhost'),
    'port': os.getenv('REDIS_PORT', 6379),
    'db': os.getenv('REDIS_DB', 0) ,
    'password': os.getenv('REDIS_PASSWORD', "redis")
}
port = os.getenv('PORT', 5000)

app = Flask(__name__)
app.config['REDIS_URL'] = f"redis://{redis_config['host']}:{redis_config['port']}/{redis_config['db']}"
CORS(app)

redis_client = FlaskRedis(app)