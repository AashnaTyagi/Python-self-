# CALCULATOR PROJECT:


print('''
                 _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              
                                              
      ''')
def add(n1,n2):
    return n1 + n2 

# opeeration= add
# print(opeeration(4,5))

def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

# make dictionary for key nd def func operations
operation={
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}

# print(operation["*"](4,8))
def calculator():
    should_accumulate=True

    num1=float(input("what is the first numb?: "))

    while should_accumulate:
        for symbol in operation:
            print(symbol)
        operation_symbol=input("pick an operation: ")
        num2=float(input("what is the second numb?: "))
        answer=operation[operation_symbol](num1,num2 )
        print(f"{num1} {operation_symbol} {num2}={answer}")
        choice=input(f"Type 'y' to continue calculating with {answer}, or Type 'n' to start new calculation: ")
        if choice=="y":
            num1=answer
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()

calculator()