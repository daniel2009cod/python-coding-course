def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def devision(x,y):
    return x / y

def multiplication(x,y):
    return x*y

print("Select operation.")

print("1.Add")

print("2.Subtract")

print("3.Multiply")

print("4.Divide")

choice = int(input("Enter your choice: "))

num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

if choice == 1:
    print(add(num1,num2))
elif choice == 2:
    print(subtract(num1,num2))
elif choice == 3:
    print(multiplication(num1,num2))
elif choice == 4:
    print(devision(num1,num2))
else:
    print("invalid choice")