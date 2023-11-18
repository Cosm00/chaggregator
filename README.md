# Chaggregator

## Description
Chaggregator is a Flask-based web application designed for integrating and managing chat services across different platforms. It currently supports Steam and Restream, offering direct integration with these services. The application also caters to chats that can be linked with a Restream account, providing a comprehensive chat management solution.

## Features
- Direct integration with Steam and Restream.
- Compatibility with various chat platforms through Restream.
- Real-time chat functionality using Flask and SocketIO.
- Dynamic configuration for service integrations.
- Multi-threaded service management for concurrent chat handling.

## Installation
To install Chaggregator:
1. Clone the repository:
`git clone [repository URL]`

2. Install necessary dependencies:
`pip install -r requirements.txt`

## First-Time Setup
On the first launch, the application will automatically create a `config.json` file. It will prompt you to enter:
- Your Steam Broadcast ID for Steam integration.
- Your Restream Embedded Chat token for Restream integration.

These details are essential for setting up the respective chat services.

## Usage
Run Chaggregator by executing:
1. The main script:
`python main.py`
2. Access the web interface at `http://localhost:38293/` or the designated port.

## Supported Chat Platforms
- **Directly Supported**: Steam and Restream.
- **Via Restream**: Any chat platform that can be integrated with Restream.

## Contributing
Contributions are welcome. Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Create a new Pull Request.

## License
MIT License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
