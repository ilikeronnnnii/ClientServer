import socket

HEADER = 64
PORT = 5051
FORMAT = 'utf-8'
DISCONNECT = "!DISCONNECT"
SERVER = "192.168.1.105"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)

send("Hello Baby")
send(DISCONNECT)