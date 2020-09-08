
example_list = []

example = input("Please enter a large number with a minimum length of 10 digits: ")

example_list = [int(d) for d in str(example)]
print (example_list)
print ('The sum of all digits = ', sum(example_list))
print (f'The sum of {example_list} is {sum(example_list)}')