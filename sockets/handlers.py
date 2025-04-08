from flask_socketio import emit

def socket_handlers(socketio):
    @socketio.on("connect")
    def handle_connect():
        emit("message", {"message": "Real-time alerts connection established"})
