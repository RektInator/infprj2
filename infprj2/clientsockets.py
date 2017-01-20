import socket
import threading

def recv_async_single_thread(ip, port, command, callback, id):
    # open client socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # attempt to connect to server
        sock.connect((ip, port))
    except:
        sock.close()
        return;

    try:
        sock.sendall(command)
        resp = str(sock.recv(1024))

        # if "inforesponse" in resp:
        callback(id)
    finally:
        sock.close()

def recv_async_single(ip, port, command, callback, id):
    recvthread = threading.Thread(target = recv_async_single_thread, args = (ip, port, command, callback, id, ))
    recvthread.start()