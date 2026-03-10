print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
def simple():
    operator = input("Enter operator")
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    # Hint: use 3 separate inputs 
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
    else:
        print("invalid operator")

def extra():
    temperature = int(input("Enter temperature in Celsius: "))
    fahrenheit = ((temperature*9)/5) + 32
    print(fahrenheit)

option = input("simple or extra calculator? ").lower
if option == 'extra':
    extra()
elif option == 'simple':
    simple()
else:
    print("invalid option")
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
