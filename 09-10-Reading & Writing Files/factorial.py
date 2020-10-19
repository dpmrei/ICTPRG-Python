factorials = open('factorials.txt', 'w')

list_factorial = []
list1 = []

for i in range (1,11):
    for a in range (1,i+1):
        list_factorial.append(a)
        list1.append(a)

        string = ('x'.join(map(str, list1)))
    
    result = 1

    for x in list_factorial:
        result = result * x

    line = (f'{i} = {string} ->  {result}')
    factorials.write(line)
    factorials.write('\n')  
    print (f'{i} = {string} ->  {result}')
    
    list_factorial = []
    list1 = []

factorials.close()