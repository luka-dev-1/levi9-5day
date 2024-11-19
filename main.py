from config import app, port
from routes import *

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port,debug=True)