# my student id = 103302783.
# magical age offset number is therefore 7 (the third last number in my id)

import time

magical_offest = 7
results = []

while True:
    first_name = input('\nPlease enter your first name:\t')
    if first_name == '':
        break
    last_name = input('\nPlease enter your last name:\t')
    age = int(input('\nPlease enter your age:\t\t'))+ magical_offest
    
    year_birth = 2020 - (age)

    email = f'{first_name[0].lower()}{last_name.lower()}@Huawow.io'

    password = f'{first_name.lower()}{last_name[0].upper()}_{str(year_birth)}'

    output = (f'{email}|{password}')

    results.append(output)
    print ('___________________________________________')
   
print ('\nOutputs:')
for item in results:
    print (item)

print ()

time.sleep (10)
