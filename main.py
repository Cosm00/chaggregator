import json
import os
import threading
import inquirer
from classes.restream import Restream
from classes.steam import Steam
from server import app, socketio

def save_config(config):
    with open('config.json', 'w') as file:
        json.dump(config, file)

def load_config():
    if os.path.exists('config.json'):
        with open('config.json', 'r') as file:
            return json.load(file)
    return []

def setup_connection(config):
    services = ['Restream', 'Steam', 'Done']
    while True:
        questions = [
            inquirer.List('service',
                          message="Select the service to setup or 'Done' to finish",
                          choices=services),
        ]
        answers = inquirer.prompt(questions)
        service = answers['service']

        if service == 'Done':
            break

        key = input(f"Enter your {service.lower()} key: ")
        # Append a new service configuration
        config.append({"service": service.lower(), "key": key})

def start_services(config):
    threads = []
    for service_config in config:
        if service_config['service'] == 'restream':
            thread = threading.Thread(target=Restream(service_config['key']).check_messages)
            threads.append(thread)
            thread.start()
        elif service_config['service'] == 'steam':
            thread = threading.Thread(target=Steam(service_config['key']).check_messages)
            threads.append(thread)
            thread.start()

    return threads

def run_flask_app():
    # Run Flask app in a separate thread with debug and reloader turned off
    socketio.run(app, debug=False, use_reloader=False, port = 38293)

def main():
    config = load_config()
    setup_connection(config)
    save_config(config)
    threads = start_services(config)

    # Start Flask server in a separate thread with debug mode off
    flask_thread = threading.Thread(target=run_flask_app)
    threads.append(flask_thread)
    flask_thread.start()

    # Wait for threads to finish if necessary
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()