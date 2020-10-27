# Write a program called 'GetEmailAddress' that will keep asking the user until 
# they enter a email address with a valid format. A Valid format of an email 
# address in this case; contains an '@', at least 1 '.' and the domain name and 
# account name is longer than 2 characters but not longer than 32 then print the 
# Email Address as a string.

# [^@]+@[^@]+\.[^@]+    is this useful?

# https://regex101.com/


def Account_Domain()



email_valid = False

while email_valid == False:
    email_input = input('Please enter your email address:\t')

    if email_input.find('@') == -1:
        print ("Please try again, a valid email must incorporate an '@' symbol.")
    
    elif email_input.find('.') == -1:
        print ("Please try again, a valid email must incorporate at least one '.' symbol.")
    
    elif:
        (account,domain_long) = email_input.split('@')
        domain = domain_long.split('.')[0]
        

print (account)
print(domain)