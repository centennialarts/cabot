#
# Twitch IRC Command Module
#

# import config
import init

# import global modules
import sys
import irc.bot
import requests

class TwitchIrc(irc.bot.SingleServerIRCBot):
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

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(
            self,
            [(server, port, 'oauth:' + token)],
            username,
            username
        )
    
    def on_welcome(self, c, e):
        print('Joining ' + self.channel)

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):

        # If a chat message starts with an exclamation point, try to run it as a command
        if e.arguments[0][:1] == '!':
            command = e.arguments[0].split(' ')[0][1:]
            fullMessage = e.arguments[0]
            
            # self.do_command(e, command)
            reply = init.executeCommandAction(
                command,
                fullMessage
            )

            if reply == None:
                return

            c = self.connection
            c.privmsg(
                self.channel,
                reply
            )
        return

# initalize main module
twitch_auth_conf = init.config['TWITCHIRC']
bot = TwitchIrc(
    twitch_auth_conf['username'],
    twitch_auth_conf['client_id'],
    twitch_auth_conf['token'],
    twitch_auth_conf['channel']
)
bot.start()