class Quiz:
    def __init__(self):
        """Initialize with a fixed supply voltage of 5V."""
        self.supply = 5  # Fixed supply voltage (Vs = 5V)
        self.led_data = self.read_file()  # Read file when class is created
        self.resistance = 0

    def read_file(self):
        """Reads LED voltage and current values from a file."""
        with open(r"text.txt", "r") as file:
            data = file.read().splitlines()
        led_values = []
        for i in range(0, len(data), 2):  # Read pairs of values

                vf = float(data[i])  # Forward voltage
                if_current = float(data[i + 1])  # Forward current
                led_values.append((vf, if_current))

        return led_values

    def calculate_resistor(self, vf, if_current):
        """Calculates resistance using R = (Vs - Vf) / If"""
        if_current_amps = if_current / 1000  # Convert mA to A
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

        if not self.led_data:
            print("No LED data found in file!")
            return

        print("Starting quiz... (Vs is always 5V)")
        for vf, if_current in self.led_data:
            self.ask_question(vf, if_current)


# Program Start
def intro():
    print("Hello students, this program will help you calculate resistance using:\n"
          "R = (Vs - Vf) / If\n")
    print("Supply voltage (Vs) is fixed at 5V.\n")

intro()

quiz = Quiz()
quiz.start_quiz()