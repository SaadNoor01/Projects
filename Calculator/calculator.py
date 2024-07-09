from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number?\n"))
  
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation from the options above: ")
    num2 = float(input("What is the next number?\n"))
    operator = operations[operation_symbol]
    answer = operator(n1 = num1, n2 = num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    cont = input(f"type 'y to continue calculating with {answer}, or type 'n to start a new calculation.: ")
  
    if cont == "y":
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
  
