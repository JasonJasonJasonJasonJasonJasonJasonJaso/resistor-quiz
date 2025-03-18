#This program is to help year 11/10s students in their pythics studies.
class quiz:
	def __init__(self, voltage, supply, current, resistance ):
		self.voltage = voltage
		self.supply = supply
		self.current = current
		self.resistance = 0

	def calculate_resistor(self):
		current_amps = self.current / 1000

	def answers(self):





def intro():
	print("Hello students, this program will make you answer questions based on the formula \n"
		  "R = (Vs - Vf) / If")

intro()
quiz.calculate_resistor()
quiz.answers()