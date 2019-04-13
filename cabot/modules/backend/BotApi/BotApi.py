#
# BotApi Module
#

# import config
import init

# import global modules
import requests
import socket

conn1 = None  # TODO: Extract this out along with the `disco` command below


class BotApi:
    def __init__(self):
        print("BotApi")

    def disco(
        self, message
    ):
        # Example Command: This is the hardcoded command to toggle the discoball light
        # TODO: Extract this and put it into its own socket external service listening thread
        conn1.send(
            "partyTime".encode("utf-8")
        )
        # conn1.close()
        return "Hopefully this worked!"

# initalize main module
twitch_conf = init.config["BOTAPI"]
bot = BotApi()

# add to commands actions
init.addCommandAction("disco", bot, "disco")

# TODO: Put this into its own thread so it doesn't lock the main thread
sock = socket.socket()
host = "192.168.1.147"  # Set this to your server's IP address
port = (
    12345
)  # This port must be available and match what the external discoball service uses
sock.bind((host, port))
sock.listen(5)

conn, addr = sock.accept()
print("Got connection from", addr)
conn.send("Thank you for connecting".encode("utf-8"))
conn1 = conn
