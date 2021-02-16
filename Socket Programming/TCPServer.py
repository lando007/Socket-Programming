from socket import *
import sys
import os

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 9876
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve ... ')
    connectionSocket, addr = serverSocket.accept()
    try:

        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        if "/grades/" in filename:
            connectionSocket.send('\nHTTP/1.1 403 Forbidden\n\n'.encode())
            connectionSocket.close()
        # Fill in security code
        else:
            f = open(filename[1:])
            print(message)
            outputdata = f.read()
            connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
    except IOError:
            connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
            connectionSocket.close()

serverSocket.close()
sys.exit()
