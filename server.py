from socket import *

serverPort = 8080
serverName = 'localhost'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print('Ready to serve')

while True :
    connectionSocket, addr = serverSocket.accept()
    kalimat = connectionSocket.recv(1024).decode()
    lowerSentence = kalimat.lower()
    connectionSocket.send(lowerSentence.encode())
    connectionSocket.close()