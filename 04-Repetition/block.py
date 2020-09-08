
list1 = []
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

print ('Please enter the number of samples collected each day this week')

for i in days:
    num1 = int(input('how many samples were collected on {}? '.format (i)))
    list1.append(num1)
    total = sum(list1)
print(list1)
print('Total collections for the week were: ', +total)   