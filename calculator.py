#program perfoming simple calucations

#defing various calculations
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y

#Calucator Interface
def calculator():
    print("Welcome to Simple Calculator!")
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4):")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    #calculator Logic
    if choice == '1':
        print("Result of Addition:-",add(num1,num2))
    elif choice == '2':
        print("Result of Subtraction:-",sub(num1,num2))
    elif choice == '3':
        print("Result of Multiplication:-",mul(num1,num2))
    elif choice == '4':
        print("Result of Division:-",div(num1,num2))
    else:
        print("Invalid Input:")

if __name__ == "__main__":
    calculator()