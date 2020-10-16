
people = open('people.txt', 'w')

while True:
    name = input('Please enter a name:\t')
    if name == '':
        break
    people.write(name)
    people.write('\n')

people.close()