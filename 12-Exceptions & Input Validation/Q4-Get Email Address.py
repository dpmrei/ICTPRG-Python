email_valid = False

while email_valid == False:

    email = input('\n[+] Please enter a valid email address.\t')
    count = 0

    while count == 0:

        # check for required components of email address
        if email.find('.') == -1 or email.find('@') == -1:
            print ("\nPlease try again.  A valid email must incorporate an '@' symbol and at least one '.'")
            break
        
        # segment the address
        email_split = email.split('@')
        dot_split = email.split('@')[1].split('.')
        length = len(dot_split)
    
        # check that there are no dead spaces on either side of '@'
        if email_split[0] == '' or email_split[1] == '':
            print ("There can not be an empty space on either side of the '@' symbol")
            break
    
        # check that the account length is correct
        elif len(email_split[0]) <3 or len(email_split[0]) > 32:
            print ('\nThe account name has to be between 3 and 32 characters long.')
            break

        # check that the mail server lenght is correct
        elif len(dot_split[0]) <3 or len(dot_split[0]) > 32:
            print ('\nThe mail server length has to be between 3 and 32 characters long.')
            break
        
        # check for space after a '.'
        elif '' in dot_split:
            print ("\nThere can not be an empty space beside a '.'")
            break
        
        # check that the email address is the correct length
        elif len(dot_split) > 3:
            print ("\nThere are too many '.' symbols.")
            break

        # check that the domain is three characters in length
        elif len(email.split('@')[1].split('.')[1]) != 3:
            print ("\nThe domain must be 3 characters in length.")
            break

        # check for spaces within email
        elif '' in email:
            print ("\nThere should not be any spaces within the email.")
            break

        else:
            count +=1

    if count == 1:
        email_valid = True


print (f"\n'{email}' is a valid email address.\n")