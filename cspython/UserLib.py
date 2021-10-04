from enum import Enum

'''
UserLib
    - Contains class User
        Stores user details
        Gets message input from user
    
    - Contains class Message
        Creates message structure with username, message content, and ID
        Validate message content
        Convert message object into string
    
    -Contains Enum MessageType
        Represents message type of either content or response
'''

class User:
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return self.username

    def GetMessageContent(self, ui):
        message = ui.GetInput()
        return message


class Message:
    def __init__(self):
        self.sendingUsername = None
        self.messageContent = None
        self.messageID = None
        self.messageType = None

    def setSendingUser(self, username):
        self.sendingUsername = username

    def setMessageContent(self, messageContent):
        self.messageContent = messageContent

    def setMessageID(self, ID):
        self.messageID = ID

    def setMessageType(self, type):
        self.messageType = type

    def IsValidContent(self, messageContent):
        #Checks that every character in the message content is a 7 bit ascii character
        #Returns true if every character has a decimal value of less than 128
        IsValidCharacter = lambda  c : ord(c)<128
        msgIsValid = all([IsValidCharacter(character) for character in messageContent])
        return msgIsValid

    def BuildMessageObjectAsString(self):
        #Converts the message object to sendable string
        #Format: msgType\x88username\x88msgContent\x88msgID
        msgString = str(self.messageType.name)+'\xAA'+str(self.messageID)+"\xAA"+self.sendingUsername
        if self.messageType==MessageType.CONTENT:
            msgString +='\xAA'+self.messageContent
       
        return msgString

    def __repr__(self):
        return f"{self.sendingUsername}: {self.messageContent}" 

class MessageType(Enum):
    CONTENT = 1
    RESPONSE = 2
    EXIT = 3