
import random

guess = int(input('Choose a random number between 1 and 20: '))

num1 = random.randint(1,20)


print ('Your guess was ' +str(guess))

print ('My number was ' +str(num1))

if guess == num1:
    print ('Wow, well done.  Great guess.')

else:
    diff = abs(int(guess - num1))
    print ('You were off by ' +str(diff))





