
user = input ('Please enter your username: ')
pswd = input ('Please enter your password: ')

if user.lower() == 'bob':
    if pswd == 'password1234':
        print ('Access Granted')
    else:
        print ('Access Denied')

elif user.lower() == 'fred':
    if pswd == 'happyPass122':
        print ('Access Granted')
    else:
        print ('Access Denied')

elif user.lower() == 'lock':
    if pswd == 'passwithlock44':
        print ('Access Granted')
    else:
        print ('Access Denied')

else:
    print ('Error, you do not have an account here')