
#                       19k-0209, 19k-1331 --------- Syed Muhammad Saad, Ali Hasnain
import threading
import socket

# localhost
host = '127.0.0.1'  
# port
port = 6789

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind server to localhost on port 6789
server.bind((host, port)) 
# listening, waiting for incoming connection
server.listen() 


print('Server is listening...')

connection, address = server.accept()
print('Connected to the client')
connection.send('Welcome'.encode('ascii'))

recvMessage=''
while True:
    recvMessage = connection.recv(1024).decode('ascii')
    print('Client: ',recvMessage)
    message = input('Type a message ')
    if (message =='end' or recvMessage=='end'):
        connection.send(message.encode('ascii'))
        connection.close()
        break
    else:
        connection.send(message.encode('ascii'))