
maths = open('maths.txt', 'w')

print ('[+]  Please provide two numbers.\n')
num = int(input('first number:\t'))
num1 = int(input('second number:\t'))
sum = num + num1

maths.write(f'The sum of {num} + {num1} = {str(sum)}')
print(f'The sum of {num} + {num1} = {str(sum)}')

maths.close()
