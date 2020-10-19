# Write a program called 'GetEmailAddress' that will keep asking the user until 
# they enter a email address with a valid format. A Valid format of an email 
# address in this case; contains an '@', at least 1 '.' and the domain name and 
# account name is longer than 2 characters but not longer than 32 then print the 
# Email Address as a string.

# [^@]+@[^@]+\.[^@]+    is this useful?

# are these tasks designed to be done without importing modules?

# https://regex101.com/

import re

email_valid = False:

while email_valid == False:
    email_input = input('Please enter your email address:\t')

    if email_input == [^@]+@[^@]+\.[^@]+