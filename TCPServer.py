from socket import *
serverPort = 12007
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while True:
     connectionSocket, addr = serverSocket.accept()
     
     message = connectionSocket.recv(1024).decode()
     print("The message received was: ", message)
     messageBytes = len(message.encode('utf-8'))
     totalMessage = "Message of " + str(messageBytes) + " bytes was received."
     connectionSocket.send(totalMessage.encode())