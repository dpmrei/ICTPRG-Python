# Write a Python function to add two numbers and return the value

# Please use the provided python script to test your function and 
# then paste the function on its own in the text field below.

# Write the function between the START and END tags
# START

def AddTwoNumbers(a,b):
    return a + b
    

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(AddTwoNumbers(1, 2) == 3))
print("Test 2 Passed: " + str(AddTwoNumbers(5, 6) == 11))
print("Test 3 Passed: " + str(AddTwoNumbers(9, 0) != 10))