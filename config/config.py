from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_redis import FlaskRedis
import os

load_dotenv()

redis_url = os.getenv('REDIS_URL')
port = os.getenv('PORT', 5000)

app = Flask(__name__)
app.config['REDIS_URL'] = redis_url
CORS(app)

redis_client = FlaskRedis(app)