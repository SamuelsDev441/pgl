import socket


class TCPServer:
    def __init__(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def look(self, server):
        server.listen()

    def take(self, server, addr):
        server.accept(addr)

    def stick(self, server, addr):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(addr)


class TCPClient:
    def __init__(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class UDPClient:
    def __init__(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
