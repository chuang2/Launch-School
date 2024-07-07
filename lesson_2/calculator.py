print("Welcome to Calculator!")
# Ask the user for the first number.
number1 = input("What is the first number? ")

# Ask the user for the second number.
number2 = input("What is the second number? ")

# Ask the user for an operation to perform.

while True:
    operation = input("What operation would you like to perform? (add=1, subtract=2, multiply=3, divide=4) ")
    if operation in ['1', '2', '3', '4']:
        break
    else:
         print("You didn't choose an appropriate number!")
# Perform the operation on the two numbers.

if operation == '1':
    output = int(number1) + int(number2)
elif operation == '2':
    output = int(number1) - int(number2)
elif operation == '3':
    output = int(number1) * int(number2)
elif operation == '4':
    output = int(number1) / int(number2)
   
# Print the result to the terminal.

print(f"The result is: {output}")

