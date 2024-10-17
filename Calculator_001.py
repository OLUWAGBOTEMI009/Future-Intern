# computing a simple calculator in python for;
# Addition
# Subtraction
# Multiplication
# Division

print("Select the operation you want to perform from the following option:")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter the number of the operation to perform:  ")

####
if (operation == "1"):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The sum  of the numbers is", num1 + num2)


if (operation == "2"):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The difference  of the numbers is", num1 - num2)

if (operation == "3"):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The product  of the numbers is", num1 * num2)


if (operation == "4"):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The result  of the numbers is", num1 / num2)


if (operation >= "5"):
    print("Invalid number of operation!")