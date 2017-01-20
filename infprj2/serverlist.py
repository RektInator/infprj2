import pygame
import button
import listbox
import database
import clientsockets
import datetime

class RawServerEntry:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.starttime = datetime.datetime.now().microsecond
        self.received = False
        self.name = ""
        self.players = 0
        self.ping = 0

servers = []

def OnServerInfoReceived(entry):
    curtime = datetime.datetime.now().microsecond

    # if ping is lower than 1000, list server in serverlist
    print("Serverresponse received for server {}:{}!".format(entry.ip, entry.port))
    entry.received = True

    entry.name = "Test lobby"
    entry.players = 0
    entry.ping = 10

def update(game):
    pass

def GetOnlineServerCount():
    idx = 0
    for x in servers:
        if x.received:
            idx += 1

    return idx

def refresh(game):
    servers.clear()

    serverips = database.execute_query("SELECT ip,port FROM servers")

    # temponary store server ips
    for s in serverips:
        # send getinfo request to server and add server to serverlist
        _rawentry = RawServerEntry(s["ip"], s["port"])
        clientsockets.recv_async_single(_rawentry.ip, _rawentry.port, b"getinfo", OnServerInfoReceived, _rawentry)
        servers.append(_rawentry)

def serverlist_gettext(game, row, column):
    if column == 0:
        return servers[row].name
    elif column == 1:
        return str(servers[row].players)
    elif column == 2:
        return str(servers[row].ping)

def serverlist_click(game, row, column):
    pass

def serverlist_update(game, box):
    serverbox.set_rows(GetOnlineServerCount())

def init(game):
    # create the serverlist 
    columns = []
    columns.append(listbox.Column(400, "Lobby"))
    columns.append(listbox.Column(200, "Spelers"))
    columns.append(listbox.Column(100, "Ping"))
    listbox.create(game, 32, 32, 800 - 64, 20, columns, serverlist_gettext, serverlist_click, serverlist_update)

    # refresh servers
    refresh(game)

def draw(game):
    listbox.draw(game)