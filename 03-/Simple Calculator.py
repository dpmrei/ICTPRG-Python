
print ('From the following operations, which would you like to perform? ')
operation = input('+ - * / ^ ')

num1 = int(input('Provide your first number '))
num2 = int(input('Provide your second number '))

if operation == '+':
    print (num1 + num2)
elif operation == '-':
    print (num1 - num2)
elif operation == '/':
    print (num1 / num2)
elif operation == '*':
    print (num1 * num2)
elif operation == '^':
    print (num1 ^ num2)

else:
    print ('sorry, incorrect input')
    