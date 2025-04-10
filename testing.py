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

        self.score = 0
        self.total_questions = len(self.led_data)


        self.red = "\033[91m"
        self.green = "\033[92m"
        self.orange = "\033[33m"
        self.blue = "\033[94m"
        self.vs_color = "\033[96m"
        self.vf_color = "\033[92m"
        self.if_color = "\033[97m"
        self.reset = "\033[0m"


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
        print("\nLet's apply the formula:")

        print(f"Your supply voltage ({self.vs_color}Vs{self.reset}): {self.vs_color}{self.supply}V{self.reset}")
        print(f"LED forward voltage ({self.vf_color}Vf{self.reset}): {self.vf_color}{vf}V{self.reset}")
        print(f"LED forward current ({self.if_color}If{self.reset}): {self.if_color}{if_current}mA{self.reset}")

        if_amps = if_current / 1000
        voltage_diff = self.supply - vf

        print("\nLet's apply the formula:")

        print(f"Step 1: Convert {self.if_color}If{self.reset} to Amps -> "
              f"{self.if_color}{if_current}mA{self.reset} ÷ 1000 = {self.if_color}{round(if_amps, 3)}A{self.reset}")

        print(f"Step 2: Subtract voltages -> {self.vs_color}Vs{self.reset} - {self.vf_color}Vf{self.reset} = "
              f"{self.vs_color}{self.supply}{self.reset} - {self.vf_color}{vf}{self.reset} = "
              f"{self.blue}{round(voltage_diff, 2)}V{self.reset}")

        print(f"Step 3: Divide by {self.if_color}If{self.reset} -> "
              f"{self.blue}{round(voltage_diff, 2)}{self.reset} ÷ {self.if_color}{round(if_amps, 3)}{self.reset} ="
              f" {self.blue}{rounded_answer}Ω{self.reset}")

    def ask_question(self, vf, if_current):
        correct_resistance = self.calculate_resistor(vf, if_current)

        while True:
            try:
                user_answer = round(float(input(f"Vf = {vf}V, If = {if_current}mA\nWhat is the resistance? ")))

                if user_answer == correct_resistance:
                    print(f"{self.green} + correct! + {self.reset}")
                    self.score += 1
                else:
                    print(f"{self.red} +  Incorrect! The correct answer is {correct_resistance}Ω. + {self.reset}")
                    self.guidelines(vf, if_current, user_answer, correct_resistance, )
                break

            except ValueError:
                print(f"{self.orange}Enter numbers instead of gibeerishes, please try again.{self.reset}")

    def start_quiz(self):

        print(f"Starting quiz... (Vs is always {self.supply}V)")
        for vf, if_current in self.led_data:
            self.ask_question(vf, if_current)
        print(f"\nQuiz is done! You got {self.score} out of {self.total_questions} correct.")

        if self.score >= self.total_questions / 2:
            print("Nice job! You will definetly pass your test!.")
        else:
            print("Keep practising! You'll get better with more tries.")


# Program Start
def intro():
    print("Hello students, this program will help you calculate resistance using:\n"
          "R = (Vs - Vf) / If\n")

    print("If answer is more than 2 decimal points, round it to 2 decimal points.")

def ask_tutorial():

    while True:
        guide = input("Would you like a tutorial? (yes/no) ").strip().lower()
        if guide == "yes":
            tutorial("\033[96m", "\033[92m", "\033[97m", "\033[0m")
            break
        elif guide == "no":
            print("\nOkay, let's start!")
            break
        else:
            print("Please enter Yes or No ")

def tutorial(vs_color, vf_color, if_color, reset):
    print("\n--- LED Resistor Calculation Tutorial ---\n")
    print("To safely use an LED, we need a resistor to limit the current.")
    print(f"Formula: R = ({vs_color}Vs{reset} - {vf_color}Vf{reset}) / {if_color}If{reset}\n")
    print("Where:")
    print(f"  {vs_color}Vs{reset} = Supply Voltage (3V or 5V)")
    print(f"  {vf_color}Vf{reset} = LED's Forward Voltage (varies by LED)")
    print(f"  {if_color}If{reset} = Forward Current in Amps")

    print("\nExample:")
    print(f"  If {vs_color}Vs{reset} = 5V, {vf_color}Vf{reset} = 2V, {if_color}If{reset} = 20mA, then:")
    print("We make sure all the values are in the correct unit and size.")
    print(
        f"  {if_color}If{reset} = 20mA but we need {if_color}If{reset} in Amps, so we divide it by 1000 to get 0.02A")
    print(f"Then we calculate R using the formula:\n")
    print(f"  R = ({vs_color}5V{reset} - {vf_color}2V{reset}) / {if_color}0.02A{reset} = 150Ω\n")
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
ask_tutorial()
supply = get_supply_voltage()
quiz = Quiz(supply)
quiz.start_quiz()