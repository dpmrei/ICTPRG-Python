
name = input('\n[+]  Please input your full name:\t')
initials = []
sep = '.'
print ()
for i in name.split():
    print (i)

for i in name.split():
    initials.append(i[0])

print (f'\nYour initials are:\t{sep.join(initials)}\n')

