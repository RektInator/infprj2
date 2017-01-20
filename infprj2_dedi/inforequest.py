import socket

def Packet_GetInfo(srv,client,args):
    # tell the client about our server
    client.send("inforesponse {} {}".format(srv.name, srv.clientcount()))

    # server info packet, we want to disconnect those clients.
    return False