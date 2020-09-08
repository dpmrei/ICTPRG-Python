
inp = 0
list1 = []

while inp != 'x':
    inp = (input('Enter some numbers (Press x to stop) '))
    (list1).append(inp)

list2 = (list1[0:-1])
list2 = list(map(int, list2))
list2 = sum(list2)
print ('The sum of your numbers is: ', +(list2))
