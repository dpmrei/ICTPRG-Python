import random
from random import randint

set_rolls = []

rolls = int(input('How many rolls would you like? '))

for roll in range(rolls):
    num = randint(1,6)
    set_rolls.append(num)

print (set_rolls)
print ('The sum of all rolls is', (sum(set_rolls)))