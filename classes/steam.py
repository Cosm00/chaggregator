import requests
import json
import time

class Steam:
    """A class to interface with Steam's chat API for a given stream."""

    def __init__(self, streamID):
        """Initialize the Steam class with a given stream ID."""
        self.checkID = "0"
        self.chatURL = f'https://steambroadcastchat.akamaized.net/chat/{streamID}/messages/{self.checkID}?chat_origin=broadcastchat3.discovery.steamserver.net:8070'
        self.s = requests.Session()
    
    def check_messages(self):
        """Continuously checks for new messages in the Steam chat and posts them to a local server."""
        while True:
            time.sleep(2.5)
            try:
                res = self.s.get(self.chatURL, headers={
                    "Host": "steambroadcastchat.akamaized.net",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Origin": "https://steamcommunity.com",
                    "Connection": "keep-alive",
                    "Referer": "https://steamcommunity.com/"
                })
                res.raise_for_status()
                json_res = res.json()

                for message in json_res.get('messages', []):
                    formattedData = {
                        "msg": message.get('msg', ''),
                        "author": message.get('persona_name', 'Unknown Author'),
                        "origin": 'steam'
                    }
                    self.s.post('http://127.0.0.1:38293/chatMessage', json=message)
                    print(str(message))

                self.checkID = str(json_res.get('next_request', "0"))

            except requests.RequestException as e:
                print(f"An error occurred: {e}")

