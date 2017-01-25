import socket
import inforequest
from packet import Packet

# packet class that holds packet information and callback
class PacketHandler:
    def __init__(self, name, callback):
        self.name = name
        self.callback = callback

packets = []

# add a packet into the packets array
def add(name, callback):
    packets.append(PacketHandler(name, callback))

# run the correct packet module for the incoming data
def run(srv, client, args):
    for p in packets:
        if p.name == args[0]:
            return p.callback(srv, client, args)

    print("[ERROR]: Packet {} is not found!".format(args[0]))
    return False

# Packet functions go here
# Packets should return True if succeeded, if you return False, the client
# that sent the packet, will be disconnected from the server.

# This packets sets the name for the current client. the server will then
# tell other clients about this change.
def Packet_Setname(srv,client,args):
    client.name = args[1]

    print("Setname packet received")

    # let other clients know about the namechange
    srv.send_all(Packet("namechange:{}:{}".format(client.index, client.name)).get())

    return True

# This packet means that a player has been connected to our lobby, let the other clients know.
def Packet_ClientConnect(srv,client,args):
    # tell the client it has been accepted.
    client.send(Packet("connectsuccess:{}:{}".format(client.index, srv.name)).get())

    for x in srv.clients:
        client.send(Packet("playerconnected:{}".format(x.index)).get())

    # let others know about our presence
    srv.send_all(Packet("playerconnected:{}".format(client.index)).get())

    # we should not get disconnected, so return True.
    return True

# This packet is fired when a client leaves the game
def Packet_Disconnect(srv,client,args):
    # let others know that we've been disconnected from the server
    srv.send_all(Packet("playerdisconnect:{}".format(client.index)).get())

    # Disconnect our shit
    return False

# init function, registers packet handlers
def init():
    # client data packets
    add("connect", Packet_ClientConnect)
    add("setname", Packet_Setname)
    add("disconnect", Packet_Disconnect)

    # serverlist packets
    add("getinfo", inforequest.Packet_GetInfo)