import curses
from cspython.UserLib import MessageType

class UserInterface:
	def __init__(self):
		self.screen = curses.initscr()
		curses.noecho()
		self.num_of_rows, self.num_cols = self.screen.getmaxyx()

	def RenderMessages(self, messageHistory):
		for row, message in enumerate(messageHistory[-self.num_of_rows+5:]):
			if message.messageType == MessageType.EXIT:
				outputString = f"{message.sendingUsername} has left the chat."
			else:
				outputString = f"{message.sendingUsername}: {message.messageContent}"
			self.screen.addstr(row,0,outputString)
			self.screen.clrtoeol()
		self.screen.refresh()

	def DisplayUserDisconnectMessage(self):
		self.screen.addstr(self.num_of_rows-4,0,"You are the only user in this chat.")
		self.screen.refresh()

	def RenderInputPromptInfo(self,chars_typed,maximum_chars,message,input_prompt):
		self.screen.addstr(self.num_of_rows-3,0,f"[{chars_typed}/{maximum_chars}]")
		self.screen.addstr(self.num_of_rows-1,0,input_prompt)
		self.screen.clrtoeol()
		self.screen.addstr(self.num_of_rows-1,len(input_prompt)+1,message)
		

	def GetInput(self):
		chars_typed = 0
		maximum_chars = 100
		message = ''
		message_sent = False
		input_prompt=">>>"
		while True:
			self.RenderInputPromptInfo(chars_typed,maximum_chars,message,input_prompt)
			
			if message_sent:
				self.screen.addstr(self.num_of_rows-1,0,input_prompt)
				self.screen.clrtoeol()
				return message

			char = self.screen.get_wch()
			if isinstance(char, str) and char.isprintable():
				if chars_typed<maximum_chars:
					chars_typed+=1
					message+=char
			elif char == '\b':
				message = message[:-1]
				if chars_typed>0:
					chars_typed-=1
			elif char =='\n':
				message_sent = True

	def Teardown(self):
		curses.endwin()
'''
import curses, time, threading

# Update the buffer, adding text at different locations
# screen.addstr(0, 0, "This string gets printed at position (0, 0)",curses.A_BLINK)
# screen.addstr(num_rows-1, 1, "Try Russian text: Привет")  # Python 3 required for unicode
# screen.addstr(4, 4, "X")
# screen.addch(5, 5, "Y")

# Changes go in to the screen buffer and only get
# displayed after calling `refresh()` to update
messages = ["Hello I am tim",
			"Hi tim its nice to meet you",
			"Its nice to mee you too, what is your name",
			"My Name is tom",
			"Hello tom!"]


screen = curses.initscr()
curses.noecho()


num_rows, num_cols = screen.getmaxyx()
curses.endwin()
print("Rows:    %d" % num_rows)
print("Columns: %d" % num_cols)

screen.addstr(num_rows-1,0,"INPUT:")

def add_message():
	for i in range(5):
		screen.addstr(i, 0, messages[i])
		curses.napms(2000)
		screen.refresh()


input_index = 7

def get_input():
	while True:
		c = screen.get_wch()
		screen.addstr(num_rows-1,input_index,c)
		screen.refresh()
		input_index+=1



curses.napms(3000)
curses.endwin()



'''


