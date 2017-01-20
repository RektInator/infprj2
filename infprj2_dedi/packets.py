import socket

# packet class that holds packet information and callback
class Packet:
    def __init__(self, name, callback):
        self.name = name
        self.callback = callback

packets = []

# add a packet into the packets array
def add(name, callback):
    packets.append(Packet(name, callback))

# run the correct packet module for the incoming data
def run(srv, client, args):
    for p in packets:
        if p.name == args[0]:
            return p.callback(srv, client, args)

# Packet functions go here
# Packets should return True if succeeded, if you return False, the client
# that sent the packet, will be disconnected from the server.

# This packets sets the name for the current client. the server will then
# tell other clients about this change.
def Packet_Setname(srv,client,args):
    client.name = args[1]

    # let other clients know about the namechange
    srv.send_all("namechange {} {}".format(client.index, client.name))

    return True

# init function, registers packet handlers
def init():
    add("setname", Packet_Setname)