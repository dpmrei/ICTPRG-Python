
date_entry = input('please enter date in DD/MM/YYYY format ')

datelist = date_entry.split('/')
print (datelist)

print ('Date:\t', datelist[0])
print ('Month:\t', datelist[1])
print ('Year:\t', datelist[2])