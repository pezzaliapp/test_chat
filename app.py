import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'questa_e_una_chiave_segreta'

# Forza WebSocket e disabilita il polling
socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode=None,  # Auto-rileva il miglior backend
    ping_interval=25,
    ping_timeout=60,
    transports=["websocket"]  # SOLO WebSocket
)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Messaggio ricevuto: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Assicurati che Render usi la porta corretta
    socketio.run(app, host='0.0.0.0', port=port, debug=True)