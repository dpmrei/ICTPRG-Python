import random

guesses = []
loop = 1

random = random.randint(0,25)

print ("\n[+] Hey there!  Let's play a little guessing game.")
print ("[+] Guess a number between 0 and 25.\n[+] I will give you 7 guesses.\n")

#print (random)

while loop <= 7:
    guess = int(input(f"\nEnter Guess #{loop}:\t\t"))
    left = 7 - loop # keep count of guesses left
    loop += 1       # keep count of guesses made
    
    # append every guess to 'guesses' list
    guesses.append(guess)
    
    # if guess not in range (0 to 25)
    if guess < 0 or guess > 25:
        print ('You are not even trying.  Bye.\n')
        break

    # if guess is correct
    if guess == random:
        print ('\nDamn. You win!')
        print ('\nIt took you', len(guesses), 'guesses.')
        print (f"Your guesses were {guesses}\n")
        break

    # if guess is too low
    elif guess < random:
        print ("Nope, it's greater than that.")
        print (f"You have {left} guesses left")

    # if guess is too high
    else:
        print ("Nope, it's less than that.")
        print (f"You have {left} guesses left")

    # end if there are more than 7 guesses (loop)    
    if loop > 7:
        print('\nAHHAHA YOU LOSE!')
        print(f'The number was {random} you fool.\n')
    
    




