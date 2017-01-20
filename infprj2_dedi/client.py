import socket

class Client:
    def __init__(self, socket):
        self.sock = socket
        
        # game variables for the current client
        self.name = ""
        self.score = 0
        self.index = -1
        # sets the index of the current client
    def set_index(self, idx):
        self.index = idx
        # sends the command to the current client
    def send(self, command):
        self.sock.send(command)

def create(serv,sock):
    # create client class
    client = Client(sock)

    # add client to the server
    serv.add_client(client)

    # start listening to client
    while True:
        data = sock.receive(1024)

        # if there is no more data to receive, disconnect the client.
        if not data:
            break

    # disconnect the client
    sock.close()