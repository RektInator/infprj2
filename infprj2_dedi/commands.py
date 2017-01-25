import socket

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
            if ":" in command:
                cmddata = command.split(":")
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

def Cmd_Kick_f(srv, args):
    pass

# register commands here
def init():
    add("start", Cmd_Start_f)
    add("kick", Cmd_Kick_f)
