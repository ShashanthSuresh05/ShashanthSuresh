# Python Program

def generate_series(n):
    if n < 1:
        return []
    elif n == 1 or n == 2:
        return [1]
    else:
        # Determine the number of odd numbers to generate
        # The series length depends on the largest odd number <= n
        max_odd = n if n % 2 == 1 else n - 1
        num_odds = (max_odd + 1) // 2  # Number of odd numbers from 1 to max_odd
        series = []
        current_odd = 1
        for i in range(num_odds):
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
            if not result:
                print("Error: No series generated for the input.")
            else:
                print(f"Output for a = {a}: {', '.join(map(str, result))}")

            # Ask if user wants to continue
            continue_calc = input("Do you want to enter another number? (yes/no): ").lower()
            if continue_calc != 'yes':
                break
        except ValueError:
            print("Error: Please enter a valid integer.")