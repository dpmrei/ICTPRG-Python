# obtain number input
digit = input ('enter a large number: ')

# create a list based on a split of the input from above
list_num = digit.split()

# create a sum of 
sum_num = sum(int(num) for num in str(digit))

print ('Sum: ' + '+'.join(str(digit)) + '=' + str(sum_num))