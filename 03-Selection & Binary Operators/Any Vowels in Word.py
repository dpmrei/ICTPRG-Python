
# obtain word and convert to lowercase
word = input ('Enter a single word: ')
lowercase = word.lower()

#create vowel count dictionary
vowel_count = {}

# vowel = count of each item in set of 'aeiou'
# count = count of vowels found in lowercase string
for vowel in 'aeiou':
    count = lowercase.count(vowel)
# In vowel_count dictionary add count value to each vowel key    
    vowel_count[vowel] = count

print (vowel_count)

counts = vowel_count.values()
total_vowels = sum(counts)

print ('There are ' +str(total_vowels) , 'vowels in your word.')