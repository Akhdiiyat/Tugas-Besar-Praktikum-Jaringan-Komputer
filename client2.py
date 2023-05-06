from socket import *
 
serverHost = 'localhost'
serverPort = 8080

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

filename = '/tes.html'
requestMessage = "GET " + filename + " HTTP/1.1\r\nHost: " + serverHost + "\r\n\r\n"
clientSocket.send(requestMessage.encode())

response = clientSocket.recv(1024).decode()

headerEnd = response.index('\r\n\r\n')
responseHeader = response[:headerEnd+4]
responseBody = response[headerEnd+4:]

print(responseHeader)
print(responseBody)

print("Client program selesai ")

clientSocket.close()
