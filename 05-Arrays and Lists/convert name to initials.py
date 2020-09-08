
name = input('please input your full name: ')
namelist = name.split(' ')
print (namelist)
initials_list = []

for item in namelist:
    initial = item[0]
    initials_list.append(initial)

print (initials_list)

print ('.'.join(initials_list))
