import socket

def Packet_GetInfo(srv,client,args):
    # debug print
    print("[INFO]: Server info request received, sending back lobby data.\n")

    # tell the client about our server
    client.send(bytes("inforesponse {} {}".format(srv.name, srv.clientcount()), 'utf-8'))

    # server info packet, we want to disconnect those clients.
    return False