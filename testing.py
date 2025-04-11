import random
# Welcome to the led resistor quiz designed for year 10/11's students for their physcis work


class Quiz:
    def __init__(self, supply):
        self.supply = supply  # Stores the users voltage input
        if supply == 3:  # Set the file name based on the supply voltage (3V or 5V)
                         # And which file to load based on the voltage choice (3V or 5V)
            file_name = "led_data_3v.txt"
        else:
            file_name = "led_data_5v.txt"

        self.supply = supply
        self.led_data = self.read_file(file_name)  # Reads the LED data from the file
        self.resistance = 0  # Placeholder for resistance calculation
        self.score = 0  # User score starts at 0
        self.total_questions = len(self.led_data)

        # Color codes for the console output (used for better readability)
        self.red = "\033[91m" # Highlights incorrect responses
        self.green = "\033[92m" # Highlights correct responses
        self.orange = "\033[33m"
        self.blue = "\033[94m"
        self.vs_color = "\033[96m" # For highlighting Voltage Supply colour
        self.vf_color = "\033[92m" # Highlighting Forward Voltage colour
        self.if_color = "\033[97m" # Highlighting Forward Current colour
        self.reset = "\033[0m" # Resets the colour to default terminal colour \
                               # so the rest of the output doesn't stay coloured
    def read_file(self, file_name):
        # Opens and reads file data line by line, storing LED Vf and If values
        with open(file_name, "r") as file:
            data = file.read().splitlines() # Splitlines function allows for spaces

        led_values = []
        for i in range(0, len(data), 2):  # Process every two lines as a pair
            vf = float(data[i])
            if_current = float(data[i + 1])
            led_values.append((vf, if_current))

        random.shuffle(led_values)  # Randomize order of questions
        return led_values

    def calculate_resistor(self, vf, if_current):
        # Calculates the resistance value using the formula
        if_current_amps = if_current / 1000  # Convert mA to A for formula
        self.resistance = round(((self.supply - vf) / if_current_amps), 0)  # Round to 0 decimal places
        return self.resistance

    def guidelines(self, vf, if_current, user_answer, rounded_answer):
        # Step by step explanation shown if student gets the question wrong
        print(f"\nFormula: R = (Vs - Vf) / If")
        print("\nLet's apply the formula:")

        #This looks confusing but is just for colour
        print(f"Your supply voltage ({self.vs_color}Vs{self.reset}): {self.vs_color}{self.supply}V{self.reset}")
        print(f"LED forward voltage ({self.vf_color}Vf{self.reset}): {self.vf_color}{vf}V{self.reset}")
        print(f"LED forward current ({self.if_color}If{self.reset}): {self.if_color}{if_current}mA{self.reset}")

        if_amps = if_current / 1000 # Converts mA to A
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
        # asks a single quiz question and loops again
        correct_resistance = self.calculate_resistor(vf, if_current)

        while True:
            try:
                # Ask the user for their answer and round it to a whole number
                user_answer = round(float(input(f"\nVf = {vf}V, If = {if_current}mA\nWhat is the resistance? ")))
                # Check if the user's answer is correct
                if user_answer == correct_resistance:
                    print(f"{self.green} + correct! + {self.reset}")
                    self.score += 1
                else:
                    # If incorrect prints feedback and calls guidelines to walk through solution
                    print(f"{self.red} +  Incorrect! The correct answer is {correct_resistance}Ω. + {self.reset}")
                    self.guidelines(vf, if_current, user_answer, correct_resistance)
                break # Exit the loop whether right or wrong

            except ValueError:
                # Catch input errors (e.g. letters instead of numbers) and prints warnings
                print(f"{self.orange}Enter numbers instead of gibeerishes, please try again.{self.reset}")

    def start_quiz(self):
        # Main quiz loop
        print(f"\n{self.blue}================ QUIZ START ================\n{self.reset}")
        print(f"(Vs is always {self.supply}V)")
        for vf, if_current in self.led_data:
            self.ask_question(vf, if_current)

        # Final score summary
        print(f"\n{self.blue}================ QUIZ COMPLETE ================\n{self.reset}")
        print(f"\nQuiz is done! You got {self.score} out of {self.total_questions} correct.")

        if self.score >= self.total_questions / 2:
            print("Nice job! You will definetly pass your test!.")
        else:
            print("Keep practising! You'll get better with more tries.")


# Program Start

def intro():
    # Intro message for users
    print("Hello students, this program will help you calculate resistance using:\n"
          "R = (Vs - Vf) / If\n")
    print("If answer is more than 2 decimal points, round it to 2 decimal points.")


def ask_tutorial():
    # Ask the user if they want a tutorial
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
    # Displays a step-by-step tutorial for how to calculate resistance
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
    print(f"  {if_color}If{reset} = 20mA but we need {if_color}If{reset} in Amps, so we divide it by 1000 to get 0.02A")
    print(f"Then we calculate R using the formula:\n")
    print(f"  R = ({vs_color}5V{reset} - {vf_color}2V{reset}) / {if_color}0.02A{reset} = 150Ω\n")
    print("--- End of Tutorial ---\n")


def get_supply_voltage():
    # Asks the user to choose supply voltage (3V or 5V) and validates input
    while True:
        supply = input("\nChoose the supply voltage: 3V or 5V ").strip().upper()
        if supply in ["3", "3V"]:
            return 3
        elif supply in ["5", "5V"]:
            return 5
        print("Wrong, please read this. Choose between 3 or 5 only.")


# Program Execution, Runs all the functions in order
intro()
ask_tutorial()
supply = get_supply_voltage()
quiz = Quiz(supply)
quiz.start_quiz()
