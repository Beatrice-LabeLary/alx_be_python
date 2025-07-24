
firstNumber = int(input("Enter the first number:"))
secondNumber = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = firstNumber + secondNumber
        print("The result is ",result)
    case "-":
        result = firstNumber - secondNumber
        print("The result is ", result)
    case "*":
        result = firstNumber * secondNumber
        print("The result is ", result)
    case "/":
        if secondNumber == 0:
            print("Cannot divide by zero.")
        else:
            result = firstNumber / secondNumber
            print("The result is ", result)
    case _:
        print("Not an operation")