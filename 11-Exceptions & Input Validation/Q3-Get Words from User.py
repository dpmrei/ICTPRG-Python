
# Write a program called 'GetWordsFromUser' that takes a Min and Max as a parameter. 
# The function then takes an input from the user and ensures that the input has at 
# least or at most the specified amount of words. Keep on asking the user until the 
# amount of words is within range, the program then outputs all words lowercase and 
# separated in a list.


input_valid = False

while input_valid == False:
    print ('\nPlease enter a sentence.  It must have a minimum of 5 words and a maximum of 10 words:\n')
    text_in = input('> ')


    count = len(text_in.split())

    if count < 5:
        print ('\n[+] Your sentence is too short.  Please try again. [+]')
        continue

    elif count > 10:
        print ('\n[+] Your sentence is too long.  Please try again. [+]')
        continue

    else:
        print('\nThank you.')
        input_valid = True
