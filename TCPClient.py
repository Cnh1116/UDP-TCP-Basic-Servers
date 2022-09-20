from socket import *

#Set up the server's IP Address and Port 
serverName = "10.159.66.233"
serverPort = 12007
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#Input the message to be sent
message = input("Input lowercase sentence:")
inputBytes = len(message.encode('utf-8'))
print("Input number of bytes: ",inputBytes)

#If the String is greater than 2048 bytes, split it into two pieces and send them seperately-------------
if(inputBytes > 1024):
    messageLength = len(message)
    print("Message Length: ",messageLength)
    #messageHalf = int(messageLength/2)

    while True:
        numberOfParses = int(input("How many pieces to parse the message into? : "))
        if (messageLength%numberOfParses == 0 and numberOfParses != 1):
            break;
        else:
            print("Message length must be divisible by parses and yield strings < 2048 Bytes.")

    for i in range (0,numberOfParses):

        stepSize = int(messageLength / numberOfParses)

        if(i != 0):
            clientSocket = socket(AF_INET, SOCK_STREAM)    
            clientSocket.connect((serverName,serverPort))#CHECK 

        clientSocket.sendto(message[(i*stepSize)+1:(i+1)*stepSize].encode(),(serverName, serverPort))
        modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
        print("Message from the PC: ", modifiedMessage.decode())
        clientSocket.close() #CHECK

        #Reopen the Socket
        #clientSocket = socket(AF_INET, SOCK_STREAM)    
        #clientSocket.connect((serverName,serverPort))#CHECK

        #clientSocket.sendto(message[(messageHalf+1):(messageLength-1)].encode(),(serverName, serverPort))
        #modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
        #print("Message from the PC: ", modifiedMessage.decode())
        #clientSocket.close()#CHECK

else:
    clientSocket.send(message.encode())
    modifiedSentence = clientSocket.recv(1024)
    print ("From Server:", modifiedSentence.decode())
    clientSocket.close()