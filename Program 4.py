# Python Program

def count_multiples(numbers):
    # Initialize dictionary with counts for multiples of 1 through 9
    result = {i: 0 for i in range(1, 10)}
    
    # Count numbers that are multiples of each number from 1 to 9
    for num in numbers:
        for divisor in range(1, 10):
            if num % divisor == 0:
                result[divisor] += 1
    
    return result

# Main program to get user input and display output
if __name__ == "__main__":
    while True:
        try:
            # Get input from user
            input_str = input("Enter numbers separated by commas (e.g., 1,2,8,9,12): ")
            # Convert input string to list of integers
            numbers = [int(x.strip()) for x in input_str.split(',')]
            
            # Generate and display the result
            result = count_multiples(numbers)
            print("Output:")
            print(result)

            # Ask if user wants to continue
            continue_calc = input("Do you want to enter another list? (yes/no): ").lower()
            if continue_calc != 'yes':
                
                break
        except ValueError:
            print("Error: Please enter valid integers separated by commas.")