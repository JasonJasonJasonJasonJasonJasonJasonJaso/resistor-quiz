#This program is to help year 11/10s students in their pythics studies.
class quiz:
	def __init__(self):
		self.voltage = 5
		self.led_data = self.read_file()
		self.resistance = 0

	def read_file(self):
		with open("text.txt", "r") as file:

			data = file.read().splitlines()
			print(data)
		led_values = []
		for i in range(0, len(data), 2):
			vf = float(data[i])
			self.icurrent_f = float(data[i + 1])
			led_values.append((vf, self.icurrent_f))

		return led_values

	def calculate_resistor(self):
		current_amps = self.current / 1000
		self.resistance = round((self.voltage - vf) / current_amps, 2)
		return self.resistance

	def answers(self):
		correct_resistance = self.calculate_resistor(vf, current)
		print(f"vf = {vf}v and If = {current}mA")
		print(f"The correct resistance is {correct_resistance} ohms.")
		user_answer = round(float(input("What is the resistance?")))
		if user_answer == self.resistance:
			print("Correct!")
		else:
			print("Incorrect!")



def intro():
	print("Hello students, this program will make you answer questions based on the formula: \n"
		  "R = (Vs - Vf) / If")


read_file = quiz()
intro()


