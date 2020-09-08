# input three numbers.  Find max of the three numbers using IF statements

num1 = int(input('enter number 1: '))
num2 = int(input('enter number 2: '))
num3 = int(input('enter number 3: '))

maxm = 0
if num1 > num2 and num1 > num3:
    maxm = num1
elif num2 > num1 and num2 > num3:
    maxm = num2
else:
    maxm = num3

print (maxm)