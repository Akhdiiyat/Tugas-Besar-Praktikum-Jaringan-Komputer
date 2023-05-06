from socket import *
#import sys
 
serverSocket = socket(AF_INET, SOCK_STREAM)

serverName = 'localhost'
serverPort = 8080 
serverSocket.bind((serverName, serverPort)) 
serverSocket.listen(1) 
 
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:
        message = connectionSocket.recv(1024).decode() 
        filename = message.split()[1]
        #if filename == '/':
            #filename = '/tes.html'
        f = open(filename[1:]) 
        outputData = f.read()

        responseHeader = "HTTP/1.1 200 OK\r\n\r\n"  + outputData
        responseHeader += "Content-Type: text/html\r\n\r\n"
        connectionSocket.send(responseHeader.encode())

        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i].encode())
        connectionSocket.send(responseHeader.encode())
        connectionSocket.close()
        
    except IOError:
        responseHeader = "'HTTP/1.1 404 Not Found\r\n\r\nFile not found'"
        responseHeader += "Content-Type: text/html\r\n\r\n"
        errorPage = "<html><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send(responseHeader.encode())
        connectionSocket.send(errorPage.encode())
        connectionSocket.close()
 
#serverSocket.close()
#sys.exit()


