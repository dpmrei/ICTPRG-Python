

user = input ('Please enter your username: ')
pswd = input ('Please enter your password: ')

if user.lower() == 'bob':
    if pswd == 'password1234':
        print ('Access Granted')
    else:
        print ('Access Denied')

elif user.lower() == 'frank':
    if pswd == 'mypassword':
        print ('Access Granted')
    else:
        print ('Access Denied')

else:
    print ('Error, you do not have an account here')
