from tkinter import *
import os

def arg(arg,self):
	self.arg = arg

class Window1(object):
	"""docstring for Window1"""
	def __init__(self, arg):
		super(Window1, self).__init__()
		self.arg = arg

		self.root = Tk()
		self.root.title("JustCreate2.0")
		self.root.geometry("1366x768")


		self.font = "Calibri"
		self.lbl = Label(self.root, text="JustCreate2.0",font=(self.font,16))
		self.lbl.pack()

		temp = Label(self.root, text="")
		temp.pack()


		self.lbl2 = Label(self.root, text="Create a Binaries folder for a game (or) an app",font=(self.font,13))
		self.lbl2.pack()

		def create_():
			self.dir_name = "Binaries"
			os.makedirs(self.dir_name)

		self.create = Button(self.root, text="Create",command=create_)
		self.create.pack()




		self.root.mainloop()

def arg(arg,self):
	self.arg = arg

class Window2(object):
	"""docstring for Window2"""
	def __init__(self, arg):
		super(Window2, self).__init__()
		self.arg = arg

		self.win = Tk()
		self.win.lbl = Label(self.win, text="Give It a sec             <||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||>")
		self.win.lbl.pack()
		self.quit = Button(self.win, text="Quit")
		self.win.mainloop()
		



if __name__ == '__main__':
	Window2(arg)
	Window1(arg)

