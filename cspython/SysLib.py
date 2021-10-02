from cspython.UserLib import User, Message, MessageType
from cspython.ServerLib import Host, Client
from os import system

'''
SysLib
    - Contains class System
        Handles the main running of the program
        Handles interaction between other classes:
            #User class - Gets user input from User
            #Server class - Provides plain text to be sent over socket
            #Message class - Builds message object from user input
'''

class System:
    def __init__(self, isHosting, port, clientAddr, username):
        self.messageHistory = []
        self.isHosting = isHosting
        self.CreateUser(username)
        self.SetUpServer(isHosting, port, clientAddr)

    def CreateUser(self,username):
        if username=='':
            username = input("Enter username: ")
        self.user = User(username)

    def SetUpServer(self, isHosting, port, clientAddr = None):
        if isHosting:
            print("Setting up host server")
            self.server = Host(port)
        else:
            print("Setting up client server")
            self.server = Client(port, clientAddr)

    def SendMessage(self, msgObj):
        #Takes message object, converts to string and bytes, send to socket server
        messageString = msgObj.BuildMessageObjectAsString()
        self.server.SendMessage(messageString)
    
    def ReceiveMessage(self):
        messageString = self.server.ReceiveMessage()
        return messageString

    def BuildContentMessage(self, user, content, ID):
        msgObj = Message()
        msgObj.setSendingUser(user)
        if not msgObj.IsValidContent(content):
            return None
        msgObj.setMessageContent(content)
        msgObj.setMessageID(ID)
        msgObj.setMessageType(MessageType.CONTENT)
        return msgObj

    def BuildResponseMessage(self, ID):
        msgObj = Message()
        msgObj.setMessageID(ID)
        msgObj.setMessageType(MessageType.CONTENT)
        return msgObj

    def ParseMessageItems(self, messageString):
        messageItems = messageItems = messageString.split('\xAA')
        messageObject = None
        if messageItems[0] == 'CONTENT':
            messageObject = self.BuildContentMessage(user = messageItems[2], content = messageItems[3], ID = messageItems[1])
        elif messageItems[0] == 'RESPONSE':
            messageObject = self.BuildResponseMessage(ID = messageItems[1])
        return messageObject

    def ConstructMessageHistoryString(self):
        historyString = ''
        for message in self.messageHistory[-50:]:
            historyString+=str(message)
            historyString+='\n'
        return historyString[:-1]

    def RefreshScreen(self):
        system('clear')
        history = self.ConstructMessageHistoryString()
        print(history)
        

    def SimpleSystemLoop(self):
        #If hosting, start by sending a message, then receive a message, and repeat
        self.RefreshScreen()
        if self.isHosting:
            while True:
                messageContent = self.user.GetMessageContent()
                messageObject = self.BuildContentMessage(self.user.username, messageContent, '1')
                self.SendMessage(messageObject)
                self.messageHistory.append(messageObject)
                self.RefreshScreen()
                recvMsg = self.ReceiveMessage()
                recvMsgObj = self.ParseMessageItems(recvMsg)
                self.messageHistory.append(recvMsgObj)
                self.RefreshScreen()
        else:
            while True:
                recvMsg = self.ReceiveMessage()
                recvMsgObj = self.ParseMessageItems(recvMsg)
                self.messageHistory.append(recvMsgObj)
                self.RefreshScreen()
                messageContent = self.user.GetMessageContent()
                messageObject = self.BuildContentMessage(self.user.username, messageContent, '1')
                self.SendMessage(messageObject)
                self.messageHistory.append(messageObject)
                self.RefreshScreen()



    #Sending
        #Get message from user
        #Build Message Object / validate message
        #Generate message string
            #Send message to server socket
        #Perform message sending validation 
    

