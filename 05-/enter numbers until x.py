entry = 0
entry_list = []
while entry != 'x':
    entry = (input('Please enter a number: '))
    if entry == 'x':
        break
    entry_list.append(int(entry))
    print (entry_list)