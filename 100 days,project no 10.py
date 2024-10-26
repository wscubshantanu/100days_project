def add(n1,n2):
    return n1 + n2

# todo: write out the other 3 function - subtract, multiply and divide
def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2


#todo: add these 4 function into a dictionary as the values. keys = "+","*","-","/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
  should_accumulate = True
  num1 = float(input("what is the first number: "))

  while should_accumulate:
    for operation in operations:
       print(operation)
    operation_symbols = input("pick an operation: ")
    num2 = float(input("what is the next number: "))
    answer = operations[operation_symbols](num1,num2)
    print(f"{num1} {operation_symbols} {num2} = {answer}")

  choice = input(f"type 'y' to continue calculating with {answer}, or type 'n' to stop: ")

  if choice == "y":
     num1 = answer
  else:
        should_accumulate = False
        print("\n" * 20)
        calculator()


calculator()


