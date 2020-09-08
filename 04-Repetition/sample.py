
total = 0
number = 0


while number != 'x':
    number = int(input('Enter some numbers (press x to stop)'))
    if number == 'x':
        break

    total += number

print (total)