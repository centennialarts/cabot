#
# Init
#

# import global modules
import configparser
import importlib

def init():
    global config
    config = configparser.ConfigParser()
    config.read('config.ini')

    global commands
    commands = {}

def addCommandAction(command, instance, function):
    if command in commands.keys():
        commands[command].append([instance, function])
    else:
        commands[command] = [[instance, function]]


def executeCommandAction(command, message):
    if command in commands.keys():
        for instanceArray in commands[command]:
            instance = instanceArray[0]
            callableMethod = getattr(instance, instanceArray[1])
            return callableMethod(message)
