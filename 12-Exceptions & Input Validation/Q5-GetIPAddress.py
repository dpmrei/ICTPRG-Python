
checks = 0

while checks != 2:
    checks = 0
    ip_input = input('Please enter a valid IPv4 address:\t')

    if ip_input.count('.') == 3:
        checks += 1
    else:
        print ("\nTry again.  A valid IPv4 address must have exactly 3 '.' separators.\n")
        checks = 0
        continue

    count = 0
    values_list = ip_input.split('.')

    if len(values_list) > 4:
        print ('There are too many numbers in your IPv4 address')
        break

    elif len(values_list) < 4:
        print ('There are too few numbers in your IPv4 address.')
        break
    
    try:
        for i in values_list:
            if int(i) >= 0 and int(i) <= 255:
                count +=1
            else:
                print("\nTry again.  Each number in an IPv4 address must be between 0 and 255\n")
                break
    except:
        print ('\nTry again, there has been an error.')
        print ("A valid IPv4 address requires 4 values and three '.' separators\n")

    if count == 4:
        checks += 1

if checks == 2:
    print (f"\nThe IPv4 address of {ip_input} is a valid address.\n")