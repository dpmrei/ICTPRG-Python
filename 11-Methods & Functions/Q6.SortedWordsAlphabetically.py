# Write a Python program that accepts a hyphen-separated sequence of words as 
# input and prints the words in a hyphen-separated sequence after sorting them 
# alphabetically called 'SortWordsAlphabetically'.

# Please use the provided python script to test your function and then paste 
# the function on its own in the text field below.

# Write the function between the START and END tags
# START

def SortWordsAlphabetically(words):
    words_split = words.lower().split('-')
    words_split.sort()
    words_joined = ('-'.join(words_split))
    print(f'\n{words_joined}')
    return words_joined
    


# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))