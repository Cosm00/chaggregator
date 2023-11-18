from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit
import json

# Avatar URLs for different platforms
avatars = {
    'steam': 'https://store.steampowered.com/favicon.ico',
    'twitch': 'https://static.twitchcdn.net/assets/favicon-32-e29e246c157142c94346.png',
    'kick': 'https://dbxmjjzl5pc1g.cloudfront.net/73d717d5-d61b-4cab-a6f5-4a395672e6f6/favicon.ico',
    'facebook': 'https://cdn.iconscout.com/icon/free/png-256/free-facebook-logo-2019-1597680-1350125.png',
    'twitter': 'https://abs.twimg.com/favicons/twitter.3.ico',
    'youtube': 'https://www.youtube.com/s/desktop/96766c85/img/favicon.ico',
    'default': 'default_avatar.png'  # Default avatar if origin is not recognized
}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Route for serving the web client
@app.route('/')
def index():
    return render_template('index.html')  # You'll need to create this HTML file

# Endpoint to handle POST requests from chat platforms
@app.route('/chatMessage', methods=['POST'])
def chat_message():
    data = request.json
    message = data.get('msg', '')
    origin = data.get('origin', 'default').lower()  # Get the origin and convert to lowercase
    avatar = avatars.get(origin, avatars['default'])  # Select the appropriate avatar or default
    socketio.emit('chat_msg', {'msg': message, 'avatar': avatar}, broadcast=True)
    return json.dumps({'success': True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    socketio.run(app, debug=False, use_reloader=False, port = 38293)