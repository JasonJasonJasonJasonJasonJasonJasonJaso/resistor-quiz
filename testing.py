
#Welcome to the led resistor quiz designed for year 10/11's students for their physcis work

class Quiz:
    def __init__(self, supply):
        self.supply = supply
        if supply == 3:
            file_name = "led_data_3v.txt"
        else:
            file_name = "led_data_5v.txt"

        self.supply = supply
        self.led_data = self.read_file(file_name)
        self.resistance = 0


    def read_file(self, file_name):
        with open(file_name, "r") as file:
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
        try:
            correct_resistance = self.calculate_resistor(vf, if_current)
            user_answer = round(float(input(f"Vf = {vf}V, If = {if_current}mA\nWhat is the resistance? ")))

            if user_answer == correct_resistance:
                print(" Correct!")
            else:
                print(f" Incorrect! The correct answer is {correct_resistance}Ω.")
        except ValueError:
            print("Enter numbers instead of gibeerishes, please try again.")

    def start_quiz(self):

        print(f"Starting quiz... (Vs is always {supply}V)")
        for vf, if_current in self.led_data:
            self.ask_question(vf, if_current)

# Program Start
def intro():
    print("Hello students, this program will help you calculate resistance using:\n"
          "R = (Vs - Vf) / If\n")
    print("If answer is more than 2 decimal points, round it to 2 decimal points.")

intro()

while True:
    supply = input("Choose the supply voltage: 3V or 5V ").strip().upper()
    if supply in ["3", "3V"]:
        supply = 3
        break
    elif supply in ["5", "5V"]:
        supply = 5
        break
    else:
        print("Wrong, please read this. Choose between 3 or 5 only.")

quiz = Quiz(supply)
quiz.start_quiz()