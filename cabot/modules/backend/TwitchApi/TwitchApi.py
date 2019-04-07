#
# Twitch API Action Module
#

# import config
import init

# import global modules
import requests
import socket

conn1 = None # TODO: Extract this out along with the `disco` command below

class TwitchApi():
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {
            'Client-ID': client_id,
            'Accept': 'application/vnd.twitchtv.v5+json'
        }
        r = requests.get(url, headers=headers).json()
        # TODO: Need better error handling for 400 error codes
        self.channel_id = r['users'][0]['_id']
    def toast(self, message):
        return 'centenToast'
    def game(self, message):
        # Poll the API to get current game.
        url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
        headers = {
            'Client-ID': self.client_id,
            'Accept': 'application/vnd.twitchtv.v5+json'
        }
        r = requests.get(url, headers=headers).json()
        return r['display_name'] + ' is currently playing ' + r['game']
    def title(self, message):
        # Poll the API the get the current status of the stream
        url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
        headers = {
            'Client-ID': self.client_id,
            'Accept': 'application/vnd.twitchtv.v5+json'
        }
        r = requests.get(url, headers=headers).json()
        return r['display_name'] + ' channel title is currently ' + r['status']
    def raffle(self, message):
        # Provide basic information to viewers for specific commands
        return "This is an example bot, replace this text with your raffle text."
    def schedule(self, message):
        return "This is an example bot, replace this text with your schedule text."
    def disco(self, message): # TODO: Extract this and put it into its own socket external service listening thread
        conn1.send('partyTime'.encode('utf-8')) # This is the hardcoded command to toggle the discoball light
        #conn1.close()
        return "Hopefully this worked!"
    

# initalize main module
twitch_conf = init.config['TWITCHAPI']
bot = TwitchApi(
    twitch_conf['username'],
    twitch_conf['client_id'],
    twitch_conf['token'],
    twitch_conf['channel']
)

# add to commands actions
init.addCommandAction('toast', bot, 'toast')
init.addCommandAction('game',bot,'game')
init.addCommandAction('title',bot,'title')
init.addCommandAction('raffle',bot,'raffle')
init.addCommandAction('schedule',bot,'schedule')
init.addCommandAction('disco', bot, 'disco')

# TODO: Put this into its own thread so it doesn't lock the main thread
sock = socket.socket()
host = '192.168.x.x' # Set this to your server's IP address
port = 12345           # This port must be available and match what the external discoball service uses
sock.bind((host,port))
sock.listen(5)

conn, addr = sock.accept()
print('Got connection from', addr)
conn.send('Thank you for connecting'.encode('utf-8'))
conn1 = conn
