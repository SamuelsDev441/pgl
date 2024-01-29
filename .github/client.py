import socket


class Client:
    client = socket.socket()

    @staticmethod
    def connect(client, address):
        client.connect(address)

    @staticmethod
    def broadcast(self, client, buffer):
        client.send(buffer)
