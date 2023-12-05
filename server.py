from server import Server

server = Server()


@server.command_manager.register("test")
def testcommand(**kwargs):
    print(kwargs)
    print("Test command")


server.run()
