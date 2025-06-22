# Python Program

def count_multiples(numbers):
    result = {i: 0 for i in range(1, 10)}
    for num in numbers:
        for divisor in range(1, 10):
            if num % divisor == 0:
                result[divisor] += 1
    
    return result

if __name__ == "__main__":
    while True:
        try:
            input_str = input("Enter numbers separated by commas (e.g., 1,2,8,9,12): ")
            numbers = [int(x.strip()) for x in input_str.split(',')]
            
            result = count_multiples(numbers)
            print("Output:")
            print(result)

            continue_calc = input("Do you want to enter another list? (yes/no): ").lower()
            if continue_calc != 'yes':
                
                break
        except ValueError:
            print("Error: Please enter valid integers separated by commas.")
