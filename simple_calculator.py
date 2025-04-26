def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    calculator()
    
    def financial_calculator():
        print("Financial Calculator")
        print("Choose an option:")
        print("1. Investment")
        print("2. Bond")

        choice = input("Enter choice (1/2): ")

        if choice == '1':
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
            time = float(input("Enter the number of years: "))
            interest_type = input("Choose interest type (simple/compound): ").lower()

            if interest_type == "simple":
                total = principal * (1 + rate * time)
                print(f"The total amount after {time} years is: {total:.2f}")
            elif interest_type == "compound":
                total = principal * (1 + rate) ** time
                print(f"The total amount after {time} years is: {total:.2f}")
            else:
                print("Invalid interest type. Please choose 'simple' or 'compound'.")

        elif choice == '2':
            present_value = float(input("Enter the present value of the house: "))
            annual_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
            months = int(input("Enter the number of months to repay: "))
            monthly_rate = annual_rate / 12

            repayment = (monthly_rate * present_value) / (1 - (1 + monthly_rate) ** -months)
            print(f"The monthly repayment amount is: {repayment:.2f}")
        else:
            print("Invalid input. Please choose '1' for Investment or '2' for Bond.")

    if __name__ == "__main__":
        calculator()
        print("\n---\n")
        financial_calculator()