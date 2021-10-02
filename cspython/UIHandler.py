import curses

class UserInterface:
	def __init__(self):
		self.screen = curses.initscr()
		self.num_of_rows, self.num_cols = self.screen.getmaxyx()
		curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

	def RenderMessages(self, messageHistory):
		for row, message in enumerate(messageHistory[-self.num_of_rows+5:]):
			self.screen.addstr(row,0,message,curses.color_pair(1))
			self.screen.clrtoeol()
		self.screen.refresh()

	def GetInput(self):
		message = ''
		message_sent = False
		while True:
			self.screen.addstr(self.num_of_rows-1,0,"INPUT")
			self.screen.clrtoeol()
			self.screen.addstr(message)
			if message_sent:
				self.screen.addstr(self.num_of_rows-1,0,"INPUT")
				self.screen.clrtoeol()
				return message
			char = self.screen.get_wch()
			if isinstance(char, str) and char.isprintable():
				message+=char
			elif char == '\x7f':
				message = message[:-1]
			elif char =='\n':
				message_sent = True

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


