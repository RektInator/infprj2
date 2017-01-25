import socket

class PacketHandler:
    def __init__(self, pack, callback):
        self.packet = pack
        self.callback = callback
    
packets = []

def register_callback(packet, callback):
    packets.append(PacketHandler(packet, callback))
        
class Client:
    def __init__(self, game):
        self.game = game
        self.host = ""
        self.port = 0
        self.sock = None
    def recvthread(self, socket, packet):
        while True:
            response = socket.recv(1024).decode("utf-8")

            # stop if the connection has been lost
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
    def send(self, cmd):
        self.sock.sendall(cmd)
    def connect(self, host, port):
        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.sock.connect((host, port))
        except:
            print("Could not connect to server at {}:{}.".format(host, port))
            self.sock.close()
            return;

        print("Connected to dedicated server at {}:{}!".format(host, port))

client = None

def init(game):
    client = Client(game)

    # This packet sets the current game state to 8 (lobby) when connectsuccess has been received
    # from the server we're currently connected to.
    register_callback("connectsuccess", lambda client,data: client.game.set_state(8))

    # this means that the lobby is full, and the match is about to begin.
    register_callback("startmatch", lambda client,data: client.game.set_state(9))

def connect(ip,port):
    client.connect(ip, port)