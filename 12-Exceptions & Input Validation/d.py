def check_email_contains(email_address, characters, min_length=2, max_length = 32):
    while True:
        for character in characters:
            if character not in email_address:
                email_address = input("Your email address must have '{}' in it\nPlease write your email address again: ".format(character))
                continue
        if len(email_address) <= min_length:
            email_address = input("email address is too short\nEnter your email address again: ")
            continue
        if len(email_address) >= max_length:
            email_address = input("Email address is too long\nEnter email address again: ")
            continue
        return email_address

email_address = check_email_contains(input("Please enter your email address\n"), "@.")