from flask import Flask, jsonify, make_response
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

@app.after_request
def after_request(response):
    """ Middleware to wrap responses with status code >= 400 into a standardized message."""
    if response.status_code >= 400:
        response_data = {
           'message': response.get_data(as_text=True),
        }
    
    return make_response(jsonify(response_data), response.status_code)  
