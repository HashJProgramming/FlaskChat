from datetime import datetime
from email import message
from socket import socket
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = 'Secret!123'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(message):
    if message != ('User connected!'):
        send(message, broadcast=True)
        print(f'User Data: {message} {datetime.now()}')


@socketio.on('connect')
def handle_connect():
    message = {'username': 'New', 'message': 'User connected!'}
    send(message, broadcast=True)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, host='localhost', debug=True)
