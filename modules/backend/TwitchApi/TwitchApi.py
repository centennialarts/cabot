#
# Twitch API Action Module
#

# import config
import init

# import global modules
import requests

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