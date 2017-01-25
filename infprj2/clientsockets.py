import socket
import threading

# this function sends a message, receives a response and then closes
# the connection to the host
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
        # send command and hope for a response
        sock.sendall(command)
        resp = sock.recv(1024).decode("utf-8")

        if "inforesponse" in resp:
            callback(id, resp)
    except:
        sock.close()
    finally:
        sock.close()

# this function creates a thread to send and receive a single command
def recv_async_single(ip, port, command, callback, id):
    recvthread = threading.Thread(target = recv_async_single_thread, args = (ip, port, command, callback, id, ))
    recvthread.setDaemon(True)
    recvthread.start()