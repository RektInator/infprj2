import socket
import sys
from packet import Packet

# command class
class Command:
    def __init__(self, name, callback):
        self.name = name
        self.callback = callback
    
# command array
commands = []

# adds commands into the command array
def add(name,callback):
    commands.append(Command(name, callback))

# command thread
def cmdthread(srv):
    while srv.isActive:
        command = input("> ")
        
        cmddata = []
        if len(command):
            if " " in command:
                cmddata = command.split(" ")
            else:
                cmddata.append(command)

            # find the correct command in the array
            for cmd in commands:
                if cmd.name == cmddata[0]:
                    # execute the callback
                    cmd.callback(srv, cmddata)
                    break

# command functions
def Cmd_Start_f(srv, args):
    srv.start_match()

# maybe later...
def Cmd_Kick_f(srv, args):
    pass

# move command
def Cmd_Move_f(srv, args):
    srv.send_all(Packet("clientmove:{}:{}:{}".format(args[1], args[2], args[3])).get())

# set name command
def Cmd_Setname_f(srv, args):
    print("[DEBUG]: Changed name of client {} to {}".format(args[1], args[2]))
    srv.send_all(Packet("namechange:{}:{}".format(args[1], args[2])).get())

# Stop the current match command
def Cmd_Stop_f(srv, args):
    srv.stop_match()

# Exit dedicated server
def Cmd_Exit_f(srv, args):
    srv.isActive = False
    
    # connect a fake client so accept gets #triggered
    dummy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dummy.connect(("", 61022))    
    dummy.close()

    #srv.sock.close()

    sys.exit()

# register commands here
def init():
    add("start", Cmd_Start_f)
    add("kick", Cmd_Kick_f)
    add("clientmove", Cmd_Move_f)
    add("setname", Cmd_Setname_f)
    add("stop", Cmd_Stop_f)
    add("exit", Cmd_Exit_f)
