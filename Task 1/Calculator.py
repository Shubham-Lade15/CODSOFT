#Simple Calculator with basic arithmetic operations
#Name : Shubham Lade
#Description : Simple calculator with basic arithmetic operations. Prompt the user to input two numbers and 
#               an operation choice. Perform the calculation and display the result.

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else : 
        return "Error: Division by zero"
    
def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def display_menu():
    print("\n-----Simple Calculator-----")
    print("1. Addition (+)")
    print("2. Substraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select operation (1-7): ")

        if choice == '7':
            print("Thank you for using calculator!")
            break

        try: 
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {substract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
        elif choice =='6':
            print(f"Result: {num1} ** {num2} = {power(num1, num2)}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()