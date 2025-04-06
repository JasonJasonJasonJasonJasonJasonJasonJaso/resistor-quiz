import random

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

        random.shuffle(led_values)
        return led_values

    def calculate_resistor(self, vf, if_current):
        if_current_amps = if_current / 1000
        self.resistance = round(((self.supply - vf) / if_current_amps), 0)
        return self.resistance

    def guidelines(self, vf, if_current, user_answer, rounded_answer):
        print(f"\nFormula: R = (Vs - Vf) / If")
        print(f"Your supply voltage (Vs): {self.supply}V")
        print(f"LED forward voltage (Vf): {vf}V")
        print(f"LED forward current (If): {if_current}mA")

        if_amps = if_current / 1000
        voltage_diff = self.supply - vf

        print("\nLets apply the formula:")
        print(f"Step 1: Convert If to Amps -> {if_current}mA ÷ 1000 = {round(if_amps, 3)}A")

        print(f"Step 2: Subtract voltages -> Vs - Vf = {self.supply} - {vf} = {round(voltage_diff, 2)}V")

        print(f"Step 3: Divide by If -> {round(voltage_diff, 2)} ÷ {round(if_amps, 3)} = {rounded_answer}Ω")

        print(f"\nYou answered: {user_answer}Ω")
        print(f"The correct answer was: {rounded_answer}Ω")

    def ask_question(self, vf, if_current):
        correct_resistance = self.calculate_resistor(vf, if_current)

        while True:
            try:
                user_answer = round(float(input(f"Vf = {vf}V, If = {if_current}mA\nWhat is the resistance? ")))

                if user_answer == correct_resistance:
                    print(" Correct!")
                else:
                    print(f" Incorrect! The correct answer is {correct_resistance}Ω.")
                    self.guidelines(vf, if_current, user_answer, correct_resistance, )
                break

            except ValueError:
                print("Enter numbers instead of gibeerishes, please try again.")

    def start_quiz(self):

        print(f"Starting quiz... (Vs is always {self.supply}V)")
        for vf, if_current in self.led_data:
            self.ask_question(vf, if_current)

# Program Start
def intro():
    print("Hello students, this program will help you calculate resistance using:\n"
          "R = (Vs - Vf) / If\n")

    print("If answer is more than 2 decimal points, round it to 2 decimal points.")

def ask_guideline():

    while True:
        guide = input("Would you like a tutorial? (yes/no) ").strip().lower()
        if guide == "yes":
            guideline()
            break
        elif guide == "no":
            print("\nOkay, let's start!")
            break
        else:
            print("Please enter Yes or No ")

def guideline():
    print("\n--- LED Resistor Calculation Tutorial ---\n")
    print("To safely use an LED, we need a resistor to limit the current.")
    print("Formula: R = (Vs - Vf) / If\n")
    print("Where:")
    print("  Vs = Supply Voltage (3V or 5V)")
    print("  Vf = LED's Forward Voltage (varies by LED)")
    print("  If = Forward Current in Amps")
    print("\nExample:")
    print("  If Vs = 5V, Vf = 2V, If = 20mA, then:")
    print("We make sure all the values are in the correct unit and size.")
    print("  If = 20mA but we need If in Amps, we divide it by 1000 to get 0.02A")
    print("Then we calculate R using the formula:\n")
    print("  R = (5V - 2V) / 0.02A = 150Ω\n")
    print("--- End of Tutorial ---\n")

def get_supply_voltage():
    while True:
        supply = input("\nChoose the supply voltage: 3V or 5V ").strip().upper()
        if supply in ["3", "3V"]:
            return 3
        elif supply in ["5", "5V"]:
            return 5
        print("Wrong, please read this. Choose between 3 or 5 only.")



intro()
ask_guideline()
supply = get_supply_voltage()
quiz = Quiz(supply)
quiz.start_quiz()