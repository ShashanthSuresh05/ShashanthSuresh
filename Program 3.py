# Python Program

def generate_series(n):
    if n < 1:
        return []
    elif n == 1 or n == 2:
        return [1]
    else:
        max_odd = n if n % 2 == 1 else n - 1
        num_odds = (max_odd + 1) // 2  
        series = []
        current_odd = 1
        for i in range(num_odds):
            series.append(current_odd)
            current_odd += 2
        return series

if __name__ == "__main__":
    while True:
        try:
            a = int(input("Enter a positive integer (a): "))
            if a <= 0:
                print("Error: Please enter a positive integer.")
                continue

            result = generate_series(a)
            if not result:
                print("Error: No series generated for the input.")
            else:
                print(f"Output for a = {a}: {', '.join(map(str, result))}")

            continue_calc = input("Do you want to enter another number? (yes/no): ").lower()
            if continue_calc != 'yes':
                break
        except ValueError:
            print("Error: Please enter a valid integer.")
