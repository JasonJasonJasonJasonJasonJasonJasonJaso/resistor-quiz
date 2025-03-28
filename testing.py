
#Welcome to the led resistor quiz designed for year 10/11's students for their physcis work

class Quiz:
    def __init__(self, supply):

        self.supply = supply
        self.led_data = self.read_file()
        self.resistance = 0
        self.supply_volt_3 ["3", "3v"]
        self.supply_volt_5 ["5", "5v"]

    def read_file(self):

        with open(r"data.txt", "r") as file:
            data = file.read().splitlines()
        led_values = []
        for i in range(0, len(data), 2):

                vf = float(data[i])
                if_current = float(data[i + 1])
                led_values.append((vf, if_current))

        return led_values

    def calculate_resistor(self, vf, if_current):
        if_current_amps = if_current / 1000
        self.resistance = round((self.supply - vf) / if_current_amps, 2)
        return self.resistance


    def ask_question(self, vf, if_current):
        correct_resistance = self.calculate_resistor(vf, if_current)
        user_answer = round(float(input(f"Vf = {vf}V, If = {if_current}mA\nWhat is the resistance? ")))

        if user_answer == correct_resistance:
            print(" Correct!")
        else:
            print(f" Incorrect! The correct answer is {correct_resistance}Ω.")

    def start_quiz(self):

        print("Starting quiz... (Vs is always 5V)")
        for vf, if_current in self.led_data:
            self.ask_question(vf, if_current)


# Program Start
def intro():
    print("Hello students, this program will help you calculate resistance using:\n"
          "R = (Vs - Vf) / If\n")
    print("Supply voltage (Vs) is fixed at 5V.")

intro()

while True:
    supply = int(input("Choose the supply voltage: 3 or 5"))

quiz = Quiz(supply)
quiz.start_quiz()