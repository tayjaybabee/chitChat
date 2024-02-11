import socket
import threading


class ChatClient:
    """A chat client supporting channels using sockets.

    Attributes:
        host (str): The server's hostname or IP address to connect to.
        port (int): The port used by the server.

    Usage example:
        client = ChatClient('localhost', 6000)
        client.start_client()
    """

    def __init__(self, host, port):
        """Initializes the chat client with the specified server host and port."""
        self.host = host
        self.port = port

    def start_client(self):
        """Connects to the chat server and starts the message sending and receiving loop."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        print("Connected to chat server. Use /join <channel_name> to join a channel.")

        threading.Thread(target=self.receive_messages).start()

        while True:
            message = input()
            self.socket.send(message.encode())

    def receive_messages(self):
        """Receives messages from the server and prints them."""
        while True:
            try:
                message = self.socket.recv(1024).decode()
                if message:
                    print(message)
                else:
                    self.socket.close()
                    break
            except Exception as e:
                print(f"Error: {e}")
                self.socket.close()
                break


if __name__ == "__main__":
    chat_client = ChatClient('ds9.local', 6000)
    chat_client.start_client()
