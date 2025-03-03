import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'questa_e_una_chiave_segreta'

socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")  # Usa "threading" invece di eventlet/gevent

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Messaggio ricevuto: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    from waitress import serve
    serve(app, host="0.0.0.0", port=port)