# Write a Python function that checks whether a passed string is 
# palindrome or not called 'IsPalindrome' that returns either True or False.
# Note: A palindrome is a word, phrase, or sequence that reads the same 
# backward as forward, e.g., madam or nurses run.

# Please use the provided python script to test your function and then paste the function on its own in the text field below.

# Write the function between the START and END tags
# START

def IsPalindrome(text):
    text_rev = text[::-1]

    if text.replace(' ','').lower() == text_rev.replace(' ','').lower():
        return True
    else:
        return False



# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))