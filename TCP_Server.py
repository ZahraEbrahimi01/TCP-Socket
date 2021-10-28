from os import path
from socket import *
from os.path import isfile

serverPort = 12111
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()

    path = 'ServerFile/' + connectionSocket.recv(1024).decode()
    if(isfile(path)):
        connectionSocket.send(str.encode("200 ok"))
        file = open(path,'rb')
        l = file.read(1024)
        while (l):
            connectionSocket.send(l)
            print('Sent ',repr(l))
            l = file.read(1024)
        file.close()

    else:
        connectionSocket.send(str.encode("404 Not Found"))

    print('Done sending')
    connectionSocket.close()
