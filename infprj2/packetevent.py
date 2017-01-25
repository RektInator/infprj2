import socket
import threading

class PacketHandler:
    def __init__(self, pack, callback):
        self.packet = pack
        self.callback = callback
    
packets = []

def register_callback(packet, callback):
    packets.append(PacketHandler(packet, callback))
        
class Client:
    def __init__(self):
        self.game = None
        self.host = ""
        self.port = 0
        self.sock = None
    def setgame(self, game):
        self.game = game
    def recvthread(self, socket):
        while True:
            response = socket.recv(1024).decode("utf-8")

            # stop if the connection has been lost
            if not response:
                print("Lost connection to the host.")
                break

            print("Received \"{}\" from host.".format(response))

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

        # create receive thread
        recvthread = threading.Thread(target = self.recvthread, args = (self.sock, ))
        recvthread.setDaemon(True)
        recvthread.start()

        print("Connected to dedicated server at {}:{}!".format(host, port))

client = Client()

def OnConnectSuccess(client, data):
    client.game.set_state(8)
    client.game.index = int(data[1])
    client.game.name = ""

def OnClientPresenceReceived(client, data):
    if int(data[1]) != client.game.index:
        print("Presence data for client {} received!", data[1])

def init(game):
    # This packet sets the current game state to 8 (lobby) when connectsuccess has been received
    # from the server we're currently connected to.
    register_callback("connectsuccess", OnConnectSuccess)

    # This packet tells us that there's another client connected
    register_callback("playerconnected", OnClientPresenceReceived)

    # this means that the lobby is full, and the match is about to begin.
    register_callback("startmatch", lambda client,data: client.game.set_state(9))

def connect(game,ip,port):
    client.setgame(game)

    # connect to the dedicated server
    client.connect(ip, port)

    # send a connect command to the dedicated server, that way it knows we're a player and not a
    # serverlist update request.
    client.send(bytes("connect", "utf-8"))
