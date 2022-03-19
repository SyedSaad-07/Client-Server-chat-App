
#                       19k-0209, 19k-1331 --------- Syed Muhammad Saad, Ali Hasnain
import threading
import socket

# localhost
host = '127.0.0.1'  
# port
port = 6789

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print('Connected to the server')

while True:
    recvMessage = client.recv(1024).decode('ascii')
    print('Server: ',recvMessage)
    message = input('Type a message ')
    if (message =='end' or recvMessage =='end'):
        client.send(message.encode('ascii'))
        client.close()
        break
    else:
        # client.send(message.encode('ascii')+time.ctime())
        client.send(message.encode('ascii'))