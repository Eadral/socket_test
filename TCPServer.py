from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, address = serverSocket.accept()
    message = connectionSocket.recv(2048)
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage)
    connectionSocket.close()
