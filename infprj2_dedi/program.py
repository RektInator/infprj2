import socket
import client
import commands
import threading
import packets

class Server:
    def __init__(self, host, port):
        # open the socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind our server to a port
        self.sock.bind(("", 61022))

        # start listening to incoming requests
        self.sock.listen(10)
  
        # Set active to true
        self.isActive = True

        # This will hold an array of connected clients
        self.clients = []

        # Server name
        self.name = ""

    # sends a message to all clients
    def send_all(self, command):
        for client in self.clients:
            if not client.sock._closed:
                client.send(command)            

    def clientcount(self):
        idx = 0
        for x in self.clients:
            idx += 1
        return idx

    def add_client(self, clnt):
        clnt.set_index(self.clientcount())
        self.clients.append(clnt)
        
        print("[INFO]: Client {} connected to the server!".format(clnt.index))

    def start_match(self):
        # let the clients know that the match has been started.
        self.send_all(bytes("startmatch", "utf-8"))
        pass
    def connection_loop(self):
        while self.isActive:
            conn, addr = self.accept()
            clientthread = threading.Thread(target = client.thread, args = (self,conn))
            clientthread.setDaemon(True)
            clientthread.start()
    def accept(self):
        return self.sock.accept()
    def shutdown(self):
        self.isActive = False

# main function of the dedicated server
def init():
    print("[INFO]: Starting up opseilen dedicated server...")

    # init the sock var
    srv = None

    # create the socket for the server
    try:
        # open the socket
        srv = Server("localhost", 61022)

    except socket.error as err:
        sock.close()
        print("[ERROR]: Dedicated server init failed, socket could not be created. Errorcode is {}.".format(err))
        quit()

    # add commands to command array
    commands.init()
    packets.init()

    # info
    print("[INFO]: Dedicated server initialization complete.");

    # Ask for a lobby name
    srv.name = input("Please enter the name of the lobby: ")

    # start command thread
    commandthread = threading.Thread(target = commands.cmdthread, args = (srv,))
    commandthread.setDaemon(True)
    commandthread.start()

    # wait for clients to connect...
    srv.connection_loop()

    # close socket
    srv.sock.close()

# Start the dedicated server
init()