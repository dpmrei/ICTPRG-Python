data_valid = False

while data_valid == False:
    try:
        number = int(input('Please enter a number:\t'))

    except ValueError:
        print('Try again')
    
    else:
        data_valid = True

print (f"Thank you, your number is '{number}'")