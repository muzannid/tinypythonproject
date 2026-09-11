def calculate (firstnum, secondnum, operation):
    if operation == "+":
        return firstnum + secondnum
    elif operation == "-":
        return firstnum - secondnum
    elif operation == "*":
        return firstnum * secondnum
    elif operation == "/":
        if secondnum == 0:
            return "Error: cannot divide with zero"
        return firstnum / secondnum
    else:
        return "Invalid operation"

continue_calculation = True

while continue_calculation:
    try:
        firstnum = float(input("Enter your first number: "))
    except ValueError:
        print("Please enter only number, not a character or symbols")
        continue
    while True:
        operation = input("Enter the operation you want to perform (+, -, *, /)\n")
        if operation not in ["+","-","*","/"]:
            print("Invalid operation, only this operation exist (+, -, *, /)")
            continue
        break
        
    try:
        secondnum = float(input("Enter your second number: "))
    except ValueError:
        print("Please enter only number, not a character or symbols")
        continue
    result = calculate( firstnum, secondnum, operation)

    print(f"the result of {firstnum} {operation} {secondnum} is {result}")

    continue_choice = input("Continue ? (y/n): ")
    if continue_choice.lower() == "y":
        continue_calculation = True
    else:
        print("Goodbye!")
        break