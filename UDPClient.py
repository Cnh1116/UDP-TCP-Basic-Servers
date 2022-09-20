from socket import *
numOfStringSplits = 2

#Set up the Server's IP Address Port Number----------
serverName = "10.159.66.233" #PC / Server IP
serverPort = 12307
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Get the User's Input--------------------------------
message = input("Enter in a message to send:")
inputBytes = len(message.encode('utf-8'))
print("Input number of bytes: ",inputBytes)

#If the String is greater than 2048 bytes, split it into two pieces and send them seperately-------------
if(inputBytes > 2048):
    messageLength = len(message)
    print(messageLength)
    
    while True:
        numberOfParses = int(input("How many pieces to parse the message into? : "))
        if (messageLength%numberOfParses == 0 and numberOfParses != 1 and messageLength/numberOfParses < 2048):
            break;
        else:
            print("Message length must be divisible by parses and yield strings < 2048 Bytes.")
    
    stepSize = int(messageLength / numberOfParses)

    for i in range(0,numberOfParses):
        clientSocket.sendto(message[i*stepSize:(i+1)*stepSize].encode(),(serverName, serverPort))
        modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
        print("Message from the PC: ", modifiedMessage.decode())

#If the string is not greater than 2048 bytes, then simply send that single string -------------------------
else:
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
    print("Message from the PC: ", modifiedMessage.decode())

