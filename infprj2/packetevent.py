import socket

class PacketHandler:
    def __init__(self, pack, callback):
        self.packet = pack
        self.callback = callback
    
packets = []

def register_callback(packet, callback):
    packets.append(PacketHandler(packet, callback))
        
class Client:
    def __init__(self):
        self.host = ""
        self.port = 0
    def recvthread(self, socket, packet):
        while True:
            response = socket.recv().decode("utf-8")

            if not response:
                break

            # split the packet data into arguments
            data = []
            if ":" in response:
                data = response.split(":")
            else:
                data.append(response)

            # run packet callback
            for x in packets:
                if x.packet == data[0]:
                    x.callback(self, data)
            
    def disconnect(self):
        pass
    def connect(self, host, port):
        self.host = host
        self.port = port

def on_packet_received(packet):
    pass

def recv_thread(socket):
    pass

def connect():
    pass
