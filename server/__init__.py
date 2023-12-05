import os
import socket
from server.src.commands import CommandManager


server = None


class Server:
    def __init__(self) -> None:
        self.command_manager = CommandManager()
        global server
        server = self
        self.cwd = os.path.dirname(os.path.abspath(__file__))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("localhost", 5060))
        self.socket = sock

    def run(self):
        from server.src.console import Console
        from server.src.listener import Listener

        self.listener = Listener()
        self.console = Console()
        self.listener.start()
        while True:
            self.console.run()
