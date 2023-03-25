from art import logo 
import os

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operation ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("First Number? "))

    for symbol in operation:
        print(symbol)

    should_contunue = True

    while should_contunue:
        operation_symbol = input("pick operation: ")
        num2 = float(input("Next Number?" ))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1 , num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculator: ") == "y":
            num1 = answer 
        else:
            should_contunue = False
            os.system('cls')
            calculator()

calculator()            
