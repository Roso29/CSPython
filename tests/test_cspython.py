from cspython import User, Message, MessageType

def test_initUser():
    user = User(username="James")
    assert user.username == "James"

def test_initMessage():
    msg = Message()

def test_setSendingUserForMessage():
    user = User(username="James")
    msg = Message()
    msg.setSendingUser(user.username)
    assert msg.sendingUsername == "James"

def test_setMessageContent():
    msg = Message()
    msg.setMessageContent("Hello, how are you?")
    assert msg.messageContent == "Hello, how are you?"

def test_buildValidMessage():
    msg = Message()
    msgString = "Hello, how are you?"
    isValidMsg = msg.IsValidContent(msgString)
    assert isValidMsg

def test_buildInValidMessage():
    msg = Message()
    msgString = "Hello, how are you?\x90"
    isValidMsg = msg.IsValidContent(msgString)
    assert not isValidMsg

def test_ConvertMessageObjToString():
    msg = Message()
    user = User(username="James")
    msg.setSendingUser(user.username)
    msg.setMessageContent("Hello, how are you?")
    msg.setMessageID(123)
    msg.setMessageType(MessageType.CONTENT)
    msgString = msg.BuildMessageObjectAsString()
    assert msgString=="CONTENT\xAA123\xAAJames\xAAHello, how are you?"

def test_ConvertAnotherMessageObjToString():
    msg = Message()
    user = User(username="Jack")
    msg.setSendingUser(user.username)
    msg.setMessageContent("Hello, I am Jack!")
    msg.setMessageID(236)
    msg.setMessageType(MessageType.CONTENT)
    msgString = msg.BuildMessageObjectAsString()
    assert msgString=="CONTENT\xAA236\xAAJack\xAAHello, I am Jack!"