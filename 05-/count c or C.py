
example = "The count of the character 'c' or 'C' in this sentence is needed."
print (example, '\n')

char_count = len(example)
c_count = example.count('c')
C_count = example.count('C')
totalC = c_count + C_count

print (f"This sentence has {char_count} characters.\n")
print (f"Number of 'c's: {c_count}")
print (f"Number of 'C's: {C_count}")
print (f"The total number of 'c's and 'C's equals {totalC}\n")