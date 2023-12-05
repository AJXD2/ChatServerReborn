from server import server


class Console:
    def __init__(self):
        self.type = "server"

    def show(self, msg):
        print(msg)

    def run(self):
        while True:
            user_input = input("Enter command: ").lower()
            if user_input == "exit":
                print("Exiting console.")
                break
            if user_input.startswith(("/", "!")):
                server.command_manager.parse(user_input, self)
                continue
