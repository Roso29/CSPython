from cspython.UserLib import User, Message, MessageType
from cspython.ServerLib import Host, Client
from cspython.UIHandler import UserInterface
from os import system
import threading
import sys

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
        self.ui = UserInterface()
        self.currentMessageID = 0
        self.hasActiveConnection = True

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

    def BuildUtilityMessage(self, user, ID, messageType):
        msgObj = Message()
        msgObj.setSendingUser(user)
        msgObj.setMessageID(ID)
        msgObj.setMessageType(messageType)
        return msgObj

    def BuildMessageObject(self, user, ID, messageType, content=None):
        if messageType == MessageType.CONTENT:
            messageObject = self.BuildContentMessage(user, content, ID)
        else:
            messageObject = self.BuildUtilityMessage(user, ID, messageType)
        return messageObject

    def ParseMessageItems(self, messageString):
        print(messageString+"!!!!!!")
        messageItems = messageString.split('\xAA')
        messageObject = None
        messageID = messageItems[1]
        typeAsString = messageItems[0]
        if messageItems[0] == 'CONTENT':
            messageObject = self.BuildContentMessage(user = messageItems[2], content = messageItems[3], ID = messageID)
        else:
            messageObject = self.BuildUtilityMessage(user = messageItems[2], ID = messageID ,messageType=MessageType[typeAsString])
        return messageObject

    def RenderScreen(self):
        self.ui.RenderMessages(self.messageHistory)

    def HandleOutgoingMessageLoop(self):
        while True:
            outgoingMessage = self.user.GetMessageContent(self.ui)
            if outgoingMessage == '$EXIT$':
                outgoingMessageObject = self.BuildMessageObject(self.user.username, self.currentMessageID, MessageType.EXIT)
            else:
                outgoingMessageObject = self.BuildMessageObject(self.user.username, self.currentMessageID, MessageType.CONTENT, outgoingMessage)

            self.currentMessageID+=1
            if self.hasActiveConnection:
                self.SendMessage(outgoingMessageObject)
            self.messageHistory.append(outgoingMessageObject)
            self.RenderScreen()
            if outgoingMessage == "$EXIT$":
                self.Teardown()
                self.ui.Teardown()
                break

    def HandleIncomingMessageLoop(self):
        while True:
            incomingMessageString = self.ReceiveMessage()
            if incomingMessageString=='':
                break
            receivedMessageObject = self.ParseMessageItems(incomingMessageString)
            self.messageHistory.append(receivedMessageObject)
            self.RenderScreen()
            if receivedMessageObject.messageType == MessageType.EXIT:
                self.ui.DisplayUserDisconnectMessage()
                self.Teardown()
                break

    def StartChatThreads(self):
        self.outgoingMessageThread = threading.Thread(target=self.HandleOutgoingMessageLoop)
        self.incomingMessageThread = threading.Thread(target=self.HandleIncomingMessageLoop)
        self.outgoingMessageThread.start()
        self.incomingMessageThread.start()
        

    def Teardown(self):
        self.hasActiveConnection = False
        if self.isHosting:
            self.server.TeardownSocket()
        sys.exit()

    #Sending
        #Get message from user
        #Build Message Object / validate message
        #Generate message string
            #Send message to server socket
        #Perform message sending validation 
    

