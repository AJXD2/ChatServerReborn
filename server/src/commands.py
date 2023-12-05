from typing import Literal, Union


class CommandExecutor:
    def __init__(
        self, type: Union[Literal["client"], Literal["server"]], sender
    ) -> None:
        self.type = type
        self.sender = sender
        if type == "client":
            self.send = self.client_send
        else:
            self.send = self.console_send

    def console_send(self, msg: str):
        self.sender.show(msg)

    def client_send(self, msg: str):
        self.sender.send(msg)


class CommandManager:
    def __init__(self) -> None:
        self.commands = {}

    def register(self, name):
        def decorator(func):
            self.commands[name.lower()] = func
            return func

        return decorator

    def parse(self, raw_input: str, sender):
        sender = CommandExecutor(sender.type, sender)

        args = raw_input.removeprefix("/").removeprefix("!").split()
        name = args[0]
        args.remove(name)

        command = self.commands.get(name)
        if command is None:
            sender.send("Invalid Command")
            return

        kwargs = {"sender": sender, "args": args}
        command(**kwargs)
