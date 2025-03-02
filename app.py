import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'questa_e_una_chiave_segreta'

# 🔹 Se eventlet è disponibile, usalo; altrimenti prova gevent, altrimenti usa threading
async_modes = ["eventlet", "gevent", "threading"]
async_mode = None

for mode in async_modes:
    try:
        socketio = SocketIO(app, cors_allowed_origins="*", async_mode=mode)
        async_mode = mode
        print(f"✅ Async mode impostato su: {async_mode}")
        break
    except ImportError:
        continue

if async_mode is None:
    raise RuntimeError("❌ Nessuna modalità async disponibile!")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"📩 Messaggio ricevuto: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)