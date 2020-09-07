

count = 0
numlist = {}

num1 = int(input('Please enter number to add.  (a negative number to end) '))

while num1 >= 0:
    count = count + num1
    num1 = int(input('enter next number. (use a negative number to end) '))

    if num1 <0:
        break
print (count)