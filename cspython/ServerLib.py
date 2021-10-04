import socket

'''
ServerLib
    - Contains class Server
        Sets up sockets
        Sends and receives plain text over sockets
        Only used to interact with the sockets - performs no verification/validation/logic
'''

class Server:
    def __init__(self, port):
        self.port = port
        self.bytesToRecv = 1024
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

class Host(Server):
    def __init__(self, port):
        super().__init__(port)
        self.SetUpSocket()
        self.hasActiveClient = False

    def SetUpSocket(self):
        numberOfClients = 1
        hostingSocket = socket.gethostbyname(socket.gethostname())
        self.serverSocket.bind((hostingSocket, self.port))
        self.serverSocket.listen(numberOfClients)
        print("Waiting for incoming connections...")
        self.clientSocket, self.clientAddress = self.serverSocket.accept()
        print(f"Connection from {self.clientAddress} established...")

    def SendMessage(self, messageString):
        self.clientSocket.sendall(bytes(messageString,"utf-8"))

    def ReceiveMessage(self):
        receivedMessageBytes = self.clientSocket.recv(self.bytesToRecv)
        receivedMessageString = receivedMessageBytes.decode("utf-8")
        return receivedMessageString    

    def TeardownSocket(self):
        self.clientSocket.close()

class Client(Server):
    def __init__(self, port, hostAddress):
        super().__init__(port)
        self.hostAddress = hostAddress
        self.SetUpSocket(port, hostAddress)

    def SetUpSocket(self, port, hostAddress):
        self.serverSocket.connect((hostAddress, port))

    def SendMessage(self, messageString):
        self.serverSocket.send(bytes(messageString,"utf-8"))

    def ReceiveMessage(self):
        receivedMessageBytes = self.serverSocket.recv(self.bytesToRecv)
        receivedMessageString = receivedMessageBytes.decode("utf-8")
        return receivedMessageString
        

'''
Use Server as a parent class
has receive and send functions and a lot of set up

client and host classes can inherit from it and add their specific server functions.

'''