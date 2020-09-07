
guess = int(input('Guess a number between 1 and 100: '))

while guess < 50 or guess > 70:
    guess = int(input('Guess again: '))

print ('Good guess')