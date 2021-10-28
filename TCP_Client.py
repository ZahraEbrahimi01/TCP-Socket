from socket import *

serverName = '127.0.0.1'
serverPort = 12111
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
name = input('Input file name : ')
path = input('Input file address : ')
nameb = str.encode(name)  # convert string to byte
clientSocket.send(nameb)
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())

if (modifiedSentence != str.encode("404 Not Found")):
    with open(path + '/' + name, 'wb') as file:
        print ('file opened')
        while True:
            print('receiving data...')
            data = clientSocket.recv(1024)
            if not data:
                break
            file.write(data)

    print(file.name)
    file.close()
    print('Successfully received the file')

clientSocket.close()
input()
