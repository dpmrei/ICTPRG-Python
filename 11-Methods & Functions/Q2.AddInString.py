# Write a Python function to add a string in-between two strings 
# and return it.

# Please use the provided python script to test your function and 
# then paste the function on its own in the text field below.

# Write the function between the START and END tags
# START

def AddInString (open, name, close):
    return f'{open}{name}{close}'
    

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE

print("Test 1 Passed: " + str(AddInString("Hello, ", "bob", ". How are you today?") == "Hello, bob. How are you today?"))
print("Test 2 Passed: " + str(AddInString("Woah there ", "frank", ", watch your step!") == "Woah there frank, watch your step!"))
print("Test 3 Passed: " + str(AddInString("Whats the , ", "meaning", " of all of this?") != "What is the meaning of all of this"))
print("Test 4 Passed: " + str(AddInString("Happy ", "Lappy", " Tappy") == "Happy Lappy Tappy"))

