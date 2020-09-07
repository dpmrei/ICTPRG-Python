import collections

list_num = []
num = input('Press key to start')
print ('starting')
while num != 'x':
    num = input('enter number: ')
    list_num.append(num)

print ([item for item, count in collections.Counter(list_num).items() if count > 1])