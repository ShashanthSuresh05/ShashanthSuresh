#Python Program

class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)  # Convert input to double
        self.b = float(b)  # Convert input to double
        self.operation = operation.lower()  # Convert operation to lowercase for consistency

    def calculate(self):
        if self.operation == "+":
            return self.a + self.b
        elif self.operation == "-":
            return self.a - self.b
        elif self.operation == "*":
            return self.a * self.b
        elif self.operation == "/":
            if self.b == 0:
                return "Error: Division by zero is not allowed"
            return self.a / self.b
        else:
            return "Error: Invalid operation. Use '+', '-', '*', or '/'"

# Function to get user input with validation
def get_user_input():
    while True:
        try:
            a = float(input("Enter the first number (a): "))
            b = float(input("Enter the second number (b): "))
            operation = input("Enter the operation (+, -, *, /): ").lower()
            return a, b, operation
        except ValueError:
            print("Error: Please enter valid numbers for a and b.")

# Main program
if __name__ == "__main__":
    print("Calculator!")
    while True:
        # Get input from user
        a, b, operation = get_user_input()

        # Create calculator instance and perform calculation
        calc = Calculator(a, b, operation)
        result = calc.calculate()

        # Display result
        print(f"Result of {a} {operation} {b} = {result}")

        # Ask if user wants to continue
        continue_calc = input("Do you want to perform another calculation? (yes/no): ").lower()
        if continue_calc != 'yes':
            break