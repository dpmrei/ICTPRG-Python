import re

# Anna's Get Valid Email Code (What modules were used?)

def ValidEmail(email):

    return re.match(r"[\w-]{2,32}@\w{2,32}\.\w{2,3}$", email)

while not pass_check:
    email = input('Enter your email:\t>>')
    valid_email = ValidEmail(email)
    if valid_email:
        print(f"Your email '{email}' is valid.")
        pass_check = True
    else:
        print (f"Your email '{email}' is invalid.  Please try again.")
        continue
    