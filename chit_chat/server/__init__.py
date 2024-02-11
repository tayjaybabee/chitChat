"""


Author: 
    Inspyre Softworks

Project:
    chitChat

File: 
    chit_chat/server/__init__.py
 

Description:
"""
import socket
import threading


class ChatServer:
    """A chat server supporting channels using sockets.

    Attributes:
        host (str): The server's hostname or IP address.
        port (int): The port used by the server to listen for incoming connections.
        clients (dict): A mapping of clients' sockets to their channel.
        channels (dict): A mapping of channel names to a list of client sockets in that channel.

    Usage example:
        server = ChatServer('localhost', 6000)
        server.start_server()
    """

    def __init__(self, host, port):
        """Initializes the chat server with the specified host and port."""
        self.host = host
        self.port = port
        self.clients = {}
        self.channels = {}

    def start_server(self):
        """Starts the server to accept incoming connections."""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Chat server with channels started on {self.host}:{self.port}. Waiting for connections...")

        while True:
            client, address = server_socket.accept()
            print(f"{address} has connected.")
            threading.Thread(target=self.handle_client, args=(client,)).start()

    def broadcast(self, message, channel):
        """Broadcasts a message to all clients in a specific channel."""
        for client in self.channels[channel]:
            client.send(f'{self.clients[client]}: {message.decode()}'.encode())  # Decode the message)

    def handle_client(self, client):
        """Handles a single client connection."""
        while True:
            try:
                message = client.recv(1024).decode()
                if message.startswith('/join'):
                    _, channel = message.split()
                    if channel not in self.channels:
                        self.channels[channel] = []
                    self.channels[channel].append(client)
                    self.clients[client] = channel
                    client.send(f"Joined channel {channel}".encode())
                elif client in self.clients:
                    self.broadcast(message.encode(), self.clients[client])
                else:
                    client.send("You must join a channel first. Use /join <channel_name>".encode())
            except Exception as e:
                print(f"Error: {e}")
                if client in self.clients:
                    self.channels[self.clients[client]].remove(client)
                    del self.clients[client]
                client.close()
                break


if __name__ == "__main__":
    chat_server = ChatServer('127.0.0.1', 6000)
    chat_server.start_server()
