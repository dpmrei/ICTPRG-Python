
while True:
    characters = input('\n[+]  Please input at least 7 random characters:\n')

    if len(characters) > 7:
        break

middle = int(len(characters)/2)

print (characters[middle-1:middle+2])