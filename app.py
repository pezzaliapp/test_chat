import eventlet
eventlet.monkey_patch()  # Applica il monkey patch per compatibilità con eventlet

import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'questa_e_una_chiave_segreta'

# Inizializza SocketIO utilizzando eventlet come async_mode
socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="eventlet",
    ping_interval=25,
    ping_timeout=60
)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Messaggio ricevuto: {msg}")
    send(msg, broadcast=True)

# Non includere il blocco "if __name__ == '__main__'" perché Gunicorn gestirà l'avvio