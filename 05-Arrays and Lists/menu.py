
food = ['Pizza', 'Pancake', 'Chips', 'Burgers', 'Pasta']

print (food, '\n')

changeout = input('Which item would you like to remove?\t').capitalize()
changein = input('Which item would you like to add in?\t').capitalize()

index1 = food.index(changeout)

print (f'\n{changeout} is located at index {index1}.  I will replace it with {changein}\n')

food[index1] = changein
print (food, '\n')
