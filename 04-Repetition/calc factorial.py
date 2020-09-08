
factorial = 1

num1 = int(input('please enter a number: '))

while num1 > 0:
    for i in range (1,num1+1):
        factorial = factorial * i

    print ('The factorial number of', +num1, f'is {factorial}.')

    break
    

