import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'questa_e_una_chiave_segreta'

# 🔹 Forza WebSocket e disabilita il polling
socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="gevent",
    ping_interval=25,  # Ogni 25 secondi invia un ping
    ping_timeout=60,  # Timeout se non riceve risposte per 60 secondi
    transports=["websocket"]  # Usa solo WebSocket
)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Messaggio ricevuto: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Porta automatica per Render
    socketio.run(app, host='0.0.0.0', port=port, debug=True)