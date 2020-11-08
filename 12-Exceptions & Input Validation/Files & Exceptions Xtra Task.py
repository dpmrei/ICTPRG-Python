# Write a program that:
# 1. Reads ages from console input
# 2. Writes the ages to a file named "ages.txt"
# 3. When "stop" is entered for age stop asking for age
# 4. After the "stop" is entered read the file and print the year of birth for each age in the file.
# 5. Also output the number of ages contained in the file
# Ensure that:
# Exceptions are used to validate age and file
# When the program is run again, it adds the new ages to the file.


age_input = 0

while age_input != 'stop':
        age_input = (input('Enter an age:\t'))
        try:
            age_input = int(age_input)
        except:
            if age_input == 'stop':
                break
            else:
                print ('That is not a valid age.')
                continue
        if int(age_input) < 1 or int(age_input) > 125:
            print ('The age must be between 1 and 125.')
        else:
            try:
                with open ('ages.txt','a') as ages:
                    ages.write(f'{age_input}\n')
            except:
                print ('error')


