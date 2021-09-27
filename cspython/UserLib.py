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
'''

class User:
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return self.username

    def GetMessageContent(self):
        print(f"{self.username}:",end='')
        message = input()
        return message


class Message:
    def __init__(self):
        self.sendingUsername = None
        self.messageContent = None
        self.messageID = None
        self.messageType = None

    def setSendingUser(self, user):
        self.sendingUsername = user.username

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
        msgString = str(self.messageType.name)+'\x88'+str(self.messageID)
        if self.messageType==MessageType.CONTENT:
            msgString += "\x88"+self.sendingUsername+'\x88'+self.messageContent
       
        return msgString

class MessageType(Enum):
    CONTENT = 1
    RESPONSE = 2