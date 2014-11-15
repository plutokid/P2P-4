import socket
import sys

SERVER_PORT = 7777
CLIENT_IP = socket.gethostname()

if len(sys.argv) != 2:
    print "Incorrect usage. Correct usage = python client.py <server_address>"
    exit(1)
server_address = sys.argv[1]

sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Connecting to server..."
sd.connect((server_address, SERVER_PORT))
print "Connected"
data = raw_input("Enter client command:\n")
sent = sd.send(data)
if sent == 0:
    print "Did not send"