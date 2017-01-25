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

    # start listening to client
    while True:
        data = sock.recv(1024).decode("utf-8")

        packetdata = data.split("{END}")

        # if there is no more data to receive, disconnect the client.
        if not data:
            # print("[INFO]: Client {} lost connection.".format(client.index))
            packets.Packet_Disconnect(serv, client, None)
            break

        for p in packetdata:
            if not p:
                break

            # run packet callbacks
            args = []
            if ":" in p:
                args = p.split(":")
            else:
                args.append(p)

            # run the packet
            if not packets.run(serv, client, args):
                break

    # show disconnected client
    print("[INFO]: Client {} disconnected.".format(client.index))

    # remove current client
    serv.clients.remove(client)

    # disconnect the client
    sock.close()