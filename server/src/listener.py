import json
from threading import Event, Thread
from time import sleep
from server import server
import ssl


class Listener(Thread):
    def __init__(self) -> None:
        super().__init__(daemon=True)
        self.socket = server.socket
        self.running = Event()

    def start(self):
        self.running.set()
        super().start()

    def run(self):
        self.socket.listen(5)
        print(f"Listening")
        while self.running.is_set():
            client, addr = self.socket.accept()
            print(f"Connection From {addr[0]}:{addr[1]}")

            try:
                # Check if the connection needs to be upgraded to SSL/TLS

                ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
                ssl_context.load_cert_chain(
                    f"{server.cwd}\\data\\keys\\server.crt",
                    f"{server.cwd}\\data\\keys\\server.key",
                )
                client = ssl_context.wrap_socket(client, server_side=True)
                print(f"Connection upgraded to SSL/TLS with {addr[0]}:{addr[1]}")

                # Send data or perform other actions with the client
                client.sendall(json.dumps({"status": "maintenance"}).encode())
                sleep(0.7)

            except ssl.SSLError as e:
                print(f"SSL/TLS error with {addr[0]}:{addr[1]}: {e}")

            finally:
                # Close the connection
                client.close()
                print(f"{addr[0]}:{addr[1]} Disconnected.")

    def stop(self):
        self.running.clear()
