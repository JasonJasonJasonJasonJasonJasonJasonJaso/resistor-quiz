#This program is to help year 11/10s students in their pythics studies.
class quiz:
	def __init__(self, voltage, supply, current, resistance ):
		self.voltage = voltage
		self.supply = supply
		self.current = current
		self.resistance = 0

	def read_file(self):
		with open("text.txt", "r") as file:
			data = file.read().splitlines()
		led_values = []
		for i in range(0, len(data), 2):
			vf = float(data[i])
			vs = float(data[i + 1])
			led_values.append((vf, vs))

		return led_values


	def calculate_resistor(self):
		current_amps = self.current / 1000
		self.resistance = round((self.supply - vf) / current_amps, 2)

	def answers(self):
		user_answer = round(float(input("What is the resistance?")))
		if user_answer == self.resistance:
			print("Correct!")
		else:
			print("Incorrect!")




def intro():
	print("Hello students, this program will make you answer questions based on the formula \n"
		  "R = (Vs - Vf) / If")

intro()

