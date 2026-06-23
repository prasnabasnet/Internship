def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else: 
        return "Odd"
    
try:
    num = int(input("Enter a number: "))
    result = even_odd(num)
    print(f"The number {num} is {result}.")
except ValueError:
    print("Please enter a valid integer.")