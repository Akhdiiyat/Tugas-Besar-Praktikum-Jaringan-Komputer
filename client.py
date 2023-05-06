from socket import *
serverName = 'localhost'
serverPort = 8080
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
kalimat = input('input kata dalam kapital : ')
clientSocket.send(kalimat.encode())
kalimatmodifikasi = clientSocket.recv(1024)
print('Dari server : ', kalimatmodifikasi.decode())
clientSocket.close()