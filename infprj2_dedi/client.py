import socket
import packets

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

def thread(serv,sock):
    # create client class
    client = Client(sock)

    # add client to the server
    serv.add_client(client)

    # let the others know about our presence
    # serv.send_all(bytes("newclient {} {}{}".format(client.index, "Speler", client.index + 1), 'utf-8'))

    # start listening to client
    while True:
        data = str(sock.recv(1024))

        # if there is no more data to receive, disconnect the client.
        if not data:
            break

        # run packet callbacks
        args = []
        if " " in data:
            args = data.split(" ")
        else:
            args.append(data)

        sock.sendall(b"getrektfam")

        # run the packet
        if not packets.run(serv, client, args):
            break

    # disconnect the client
    sock.close()