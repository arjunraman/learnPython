## Notes for Exam: UDP
# on server

import socket

def udp_echo_service():
    s = socket.socket(type=socket.SOCK_DGRAM)
    s.bind(('127.0.0.1',12345))
    # the loop keeps the service alive
    while True:
        data, address = s.recvfrom(4096)
        print('received',data,'from',address)
        s.sendto(data,address)


#on client

import socket
def udp_echo_client():
    s = socket.socket(type=socket.SOCK_DGRAM)
    # the sendto was changed to prompt the user for input
    # Note the encoding; remember we have to send a bytes object
    s.sendto(input("Text to send: ").encode("ascii"),('10.50.162.86',7777)) #this is important
    data,address = s.recvfrom(4096)
    print(data,'received from',address)
    
udp_echo_client()


"""
Notes for Exam:
1. Identify if its TCP or UDP (likely TCP)
2. Check the following:
    a. socket.socket
    b. import socket
    c. bind - tuple
    d. check for 'b' - focues on bytes if "input() is not there
    e. check ip of server
    f. check port of server
    
"""
# Notes for EXAM: TCP

# on server
import socket

def tcp_qotd_service():
    s = socket.socket()
    s.bind(('',12345))
    s.listen()
    # the loop makes it work continously; i.e. it is now a "service"
    while True:
        client_socket, address = s.accept()
        quote = b'Object oriented programs are offered as alternatives to correct ones.'
        # .sendall() will divide up your message if it is larger than the buffer,
        # it sends until complete
        client_socket.sendall(quote)
        client_socket.close()
"""
Notes for Exam:
1. Identify if its TCP vs. UDP (likely TCP)"
2. Check the following:
    a. socket.socket (note for TCP this is always by default empty.  there is no SOCK_STREAM like with UDP SOCK_DATAGRAM)
    b. import socket
    c. bind - tuple
    d. check for 'b' - focues on bytes if "input() is not there
    e. check ip of server
    f. check port of server
    f. check for .listen and .accept on server

"""


# on client
import socket

def tcp_qotd_client():
    s = socket.socket()
    s.connect(('127.0.0.1',12345))
    msg = bytearray() # <- A bytearray to store the parts of message
    chunk = s.recv(4) # <- Receive the first message piece
    while chunk:
        print(msg) # <- To see the message grow
        msg.extend(chunk) # <- adds to bytearray
        chunk = s.recv(4) # <- receives next chunk of msg
    print(msg) # <- prints the completed message

"""
Notes for Exam:
1. Identify if its TCP vs. UDP (likely TCP)"
2. Check the following:
    a. SOCK_STREAM
    b. import socket 
    c. check s.recv
    d. check ip
    e. check port
    f. check for .listen and .accept on server

"""