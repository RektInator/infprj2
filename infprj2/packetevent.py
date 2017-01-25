import socket
import threading
import player

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

            print("[DEBUG]: Received \"{}\" from host.".format(response))

            pks = response.split("{END}")
            for packet in pks:
                # check if packet even has data.
                if not packet:
                    continue

                # split the packet data into arguments
                packetdata = []
                if ":" in packet:
                    packetdata = packet.split(":")
                else:
                    packetdata.append(packet)

                # run packet callback
                for x in packets:
                    if x.packet == packetdata[0]:
                        x.callback(self, packetdata)
            
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

def DoesPlayerExist(game, idx):
    for x in game.players:
        if x.index == idx:
            return True

    return False

def OnConnectSuccess(client, data):
    # clear existing players
    client.game.players.clear()

    # set game data
    client.game.set_state(8)
    client.game.index = int(data[1])
    client.game.name = ""
    client.game.lobbyname = data[2]

def OnClientPresenceReceived(client, data):
    if not DoesPlayerExist(client.game, int(data[1])):
        # debug output
        print("Presence data for client {} received!".format(data[1]))

        # create player entry
        plr = player.Player(client.game)
        plr.setindex(int(data[1]))
        plr.setmp(True)

        # append player
        client.game.players.append(plr)

def OnClientDisconnected(client, data):
    if DoesPlayerExist(client.game, int(data[1])):
        # get player
        plr = client.game.get_player_by_index(int(data[1]))

        # debug output
        print("Player {} ({}) has left the lobby.".format(plr.index, plr.name))

        # remove the client from our internal array
        client.game.players.remove(plr)

def OnClientNameReceived(client, data):
    plr = client.game.get_player_by_index(int(data[1]))
    plr.name = data[2]
    print("Name for client {} changed to {}.".format(data[1], data[2]))

def init(game):
    # This packet sets the current game state to 8 (lobby) when connectsuccess has been received
    # from the server we're currently connected to.
    register_callback("connectsuccess", OnConnectSuccess)

    # This packet tells us that there's another client connected
    register_callback("playerconnected", OnClientPresenceReceived)

    # This packet tells us that a client has been disconnected
    register_callback("playerdisconnect", OnClientDisconnected)
    
    # This packet will keep us up-to-date about other clients their names
    register_callback("namechange", OnClientNameReceived)

    # this means that the lobby is full, and the match is about to begin.
    register_callback("startmatch", lambda client,data: client.game.set_state(9))

def connect(game,ip,port):
    game.sockets.setgame(game)

    # connect to the dedicated server
    game.sockets.connect(ip, port)

    # send a connect command to the dedicated server, that way it knows we're a player and not a
    # serverlist update request.
    game.sockets.send(bytes("connect", "utf-8"))
