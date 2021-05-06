from growbox import socketio

@socketio.on("message")
def handle_message(msg):
    print(msg)