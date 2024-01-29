import socket


class Server:
    def __init__(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def look(self, server):
        server.listen()

    def take(self, server, addr):
        server.accept(addr)

    def stick(self, server, addr):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(addr)
