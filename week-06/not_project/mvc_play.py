#[----------------------] 0%
#[############----------] 50%
#[######################] 100%
# Model
#  - progress
#  - setProgress()
# View
#  - display()
# Controller
#  - init
import os

class ProgressModel:
	def __init__(self):
		self.progress = 0
		# Complete event callback function
		self.complete = lambda:x

	def increment(self):
		if self.progress < 100:
			self.progress += 1
		else:
			self.complete()

class ProgressView:
	def clearScreen(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def display(self,progress):
		self.clearScreen()
		toDisplay = '['
		for i in range(50):
			if i < progress//2:
				toDisplay += '#'
			else:
				toDisplay += '-'
		toDisplay += '] ' + str(progress) + '%'
		print(toDisplay)

	def showComplete(self):
		print('YAY, We are done')

class ProgressController:
	def __init__(self):
		self.running = True
		self.model = ProgressModel()
		self.view = ProgressView()
		self.view.clearScreen()
		self.model.complete = self.complete
		self.loop()

	def complete(self):
		self.view.showComplete()
		self.running = False

	def loop(self):
		while self.running:
			input()
			self.model.increment()
			self.view.display( self.model.progress )

		self.view.showComplete()

progressBar = ProgressController()
