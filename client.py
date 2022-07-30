import socket
import select
import sys
from donkey import donkey_say 
from elephent import elephent_say
def print_funny(message, animal):
    if animal == "donkey":
        donkey_say(message)
    elif animal == "elephent":
        elephent_say(message)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 4:
    print ("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))
 
you = ""
if sys.argv[3] == "d":
    you = "donkey"
    other = "elephent"
elif sys.argv[3] == "e" :
    you = "elephent"
    other = "donkey"
else:
    print("use d for donkey or e for elephent")
    exit()

while True:
 
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]
 
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        print("*")
        if socks == server:
            message = socks.recv(2048).decode()
            print_funny(message, other)
        else:
            message = sys.stdin.readline()
            server.send(message.encode())
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
            print_funny(message, you)
server.close()
