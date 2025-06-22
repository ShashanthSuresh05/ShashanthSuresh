# Python Program

def generate_series(n):
    series = []
    current_odd = 1
    for i in range(n):
        series.append(current_odd)
        current_odd += 2
    return series

# Main program to get user input and display output
if __name__ == "__main__":
    while True:
        try:
            # Get input from user
            a = int(input("Enter a positive integer (a): "))
            if a <= 0:
                print("Error: Please enter a positive integer.")
                continue

            # Generate and display the series
            result = generate_series(a)
            print(f"Output for a = {a}: {', '.join(map(str, result))}")

            # Ask if user wants to continue
            continue_calc = input("Do you want to enter another number? (yes/no): ").lower()
            if continue_calc != 'yes':
                break
        except ValueError:
            print("Error: Please enter a valid integer.")