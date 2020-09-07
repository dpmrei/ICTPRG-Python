
currentyr = 2020
born = int(input('Good evening, what is your year of birth? '))

age = int(currentyr - born)
print ('You are ' +str(age), 'years old')

if age >= 18:
    print ('Come on in and have a drink.')
else:
    print ('Go away child')
    

