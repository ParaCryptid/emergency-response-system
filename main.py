from flask import Flask
from flask_socketio import SocketIO
from routes.api import api_routes
from sockets.handlers import socket_handlers

from config.env import Config

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app)

# Register routes and sockets
api_routes(app)
socket_handlers(socketio)

import os
if __name__ == "__main__":
    if os.getenv("GUI_MODE", "False") == "True":
        from utils.gui import EmergencyGUI
        EmergencyGUI().run()
    else:
    socketio.run(app, host="0.0.0.0", port=5000)
