# Write a program called 'GetPassword' that will keep asking a user to enter a password 
# (and confirm the password) until the following criteria is met:

# contains at least one of each:
# a lowercase letter
# an uppercase letter
# a number
# a symbol
# is at least 7 characters long
# does not contain the word 'password'
# The program will then output "valid password".

import re

pass_valid = False

print('\nPassword Conditions:')
print('Your password should contain at least one uppercase and one lowercase letter')
print('Your password should also contain at least one number and one symbol')
print('The password must be a minimum of 7 characters long')
print("Finally, your password must not be the word 'password'")

while pass_valid == False:
    
    password = input('\n[+]  Please submit a password for your account:\t')

    if len(password) < 7:
        print('The password must be a minimum of 7 characters long')
        continue
    elif password.lower() == 'password':
        print("The password must not be the word 'password'")
        continue
    elif not re.search('[a-z]', password):
        print('The password must contain at least one lowercase letter')
        continue
    elif not re.search('[A-Z]', password):
        print('The password must contain at least one uppercase letter')
        continue
    elif not re.search('[0-9]', password):
        print('The password must contain at least one number')
        continue
    elif not re.search('[!@#$%^&*()-_+=]', password):
        print('The password must contain at least one symbol')
        continue
    else:
        pass_valid = True
        break

print ('Your password is accepted.')