#
# BotNet Command Module
#

# import config
import init

# import global modules
import sys
import irc.bot
import requests

class BotNet(irc.bot.SingleServerIRCBot):
    def __init__(self):
        return

# initalize main module
botNet = BotNet()
botNet.start()
