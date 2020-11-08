
with open('people.txt', 'r') as source:
    for line in source.readlines():
        name, surname, age = line.strip().split('|')
        #print (f'name = {name}, surname = {surname}, age = {age}')

        with open('userpass.txt', 'a') as output:
            if name.lower()[0] == 'b':
                continue
            elif int(age) > 50:
                continue 
            else:
                result = (f'{name.lower()[0]}{surname.lower()}@DodnGy.net|!{2020-int(age)}{surname}{name[0]}_')
                output.write(f'{result}\n')
        