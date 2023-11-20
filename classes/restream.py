import websocket
import requests
import json
import time

class Restream:
    def __init__(self, chatToken):
        self.webSocketURL = f'wss://backend.chat.restream.io/ws/embed?token={chatToken}'
        self.s = requests.Session()

    def is_chat_message(self, messageData):
        # Check if the message is a chat message
        return (messageData.get('action') == 'event' and
                'eventPayload' in messageData.get('payload', {}) and
                'text' in messageData['payload'].get('eventPayload', {}))

    def parse_origin(self, connectionIdentifier):
        platforms = ["twitch", "kick", "youtube", "facebook", "steam", "twitter"]
        for platform in platforms:
            if platform in connectionIdentifier.lower():
                return platform
        return "unknown"

    def on_message(self, ws, message):
        messageData = json.loads(message)
        if self.is_chat_message(messageData):
            eventPayload = messageData.get('payload', {}).get('eventPayload', {})
            formattedData = {
                "msg": eventPayload.get('text', ''),
                "author": eventPayload.get('author', {}).get('displayName', eventPayload.get('author', {}).get('name', 'Unknown Author')),
                "origin": self.parse_origin(messageData.get('payload', {}).get('connectionIdentifier', ''))
            }
            self.s.post('http://127.0.0.1:38293/chatMessage', json=formattedData)
            print("Chat Message:", formattedData)
        else:
            print("Non-Chat Message:", messageData)

    def on_error(self, ws, error):
        print("Error:", error)

    def on_close(self, ws, close_status_code, close_msg):
        print("### closed ###")
        print('Reconnecting...')
        time.sleep(2.5)
        self.check_messages()

    def on_open(self, ws):
        print("Connection opened")

    def check_messages(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(self.webSocketURL,
                                    on_open=self.on_open,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)

        ws.run_forever()
