from .UserLib import User, Message, MessageType

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
    def __init__(self, isHosting):
        self.messageHistory = []
        self.isHosting = isHosting
        self.user = User("James")

    def SendMessage(self, msgObj):
        #Takes message object, converts to string and bytes, send to socket server
        messageString = msgObj.BuildMessageObjectAsString()
        #server.SendOverSocket(messageString)
    
    def BuildContentMessage(self, content, ID):
        msgObj = Message()
        msgObj.setSendingUser(self.user)
        if not msgObj.IsValidContent(content):
            return None
        msgObj.setMessageContent(content)
        msgObj.setMessageID(ID)
        msgObj.setMessageType(MessageType.CONTENT)
        return msgObj

    def BuildResponseMessage(self, ID):
        msgObj = Message()
        if not msgObj.IsValidContent(content):
            return None
        msgObj.setMessageContent(content)
        msgObj.setMessageID(ID)
        msgObj.setMessageType(MessageType.CONTENT)
        return msgObj


    #Sending
        #Get message from user
        #Build Message Object / validate message
        #Generate message string
            #Send message to server socket
        #Perform message sending validation 
    
    