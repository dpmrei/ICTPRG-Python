

count = 0

pocketnum = int(input('enter a pocket number: '))

while pocketnum > 0 and pocketnum < 37:
    if pocketnum == 0:
        pocketcol = 'green'
    elif pocketnum > 0 and pocketnum <= 10:
        if pocketnum % 2 == 0:
            pocketcol = 'black'
        else:
            pocketcol = 'blue'
    elif pocketnum > 10 and pocketnum <= 18:
        if pocketnum % 2 == 0:
            pocketcol = 'blue'
        else:
            pocketcol = 'black'
    elif pocketnum > 18 and pocketnum <= 28:
        if pocketnum % 2 == 0:
            pocketcol = 'black'
        else:
            pocketcol = 'blue'
    elif pocketnum > 28 and pocketnum <= 36:
        if pocketnum % 2 == 0:
            pocketcol = 'blue'
        else:
            pocketcol = 'black'

    print (pocketcol)

    pocketnum = int(input('please enter another pocket number: '))

    count = count + 1

print (f'you entered a number {count} times.')
