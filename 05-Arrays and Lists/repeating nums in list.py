
entry = 0
entry_list = []
dict1 = {}

while entry != 'x':
    entry = (input('Please enter a number: '))
    if entry == 'x':
        break
    entry_list.append(int(entry))

print (entry_list)

for num in entry_list:
    if entry_list.count(num) > 1:
        dict1[num] = entry_list.count(num)
    
for key in dict1:
    print (key, 'appears', dict1[key], 'times')