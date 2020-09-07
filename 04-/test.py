

exit = False

while exit == False:

    try:
        value = input('please enter a number:\n')
        valint = int(value)
        exit = True
    except:
        print (value + ' is not a number\n')
       

print (valint)