from socket import *

serverPort = 12307
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive...")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    messageBytes = len(modifiedMessage.encode('utf-8'))
    print("The message received was: ", modifiedMessage)
    print("Number of Bytes: ", messageBytes)
    totalMessage = "Message of " + str(messageBytes) + " bytes was received."
    serverSocket.sendto(totalMessage.encode(),clientAddress)