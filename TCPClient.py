from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = bytes(input("Input lowercase sentence: "), encoding="UTF-8")
clientSocket.send(message)
receivedMessage = clientSocket.recv(2048)
print(receivedMessage)
clientSocket.close()


