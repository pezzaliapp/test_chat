import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'questa_e_una_chiave_segreta'

# Forziamo l'utilizzo di gevent come async mode (se usi gevent)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="gevent")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Messaggio ricevuto: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    # Usa una porta diversa, ad esempio 5001
    port = int(os.environ.get("PORT", 5001))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)