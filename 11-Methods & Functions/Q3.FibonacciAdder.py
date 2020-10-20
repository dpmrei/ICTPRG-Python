# Write a Python function that returns the sum of all numbers 
# of Fibonacci to the provided count. 

# Please use the provided python script to test your function 
# and then paste the function on its own in the text field below.

# Write the function between the START and END tags
# START

def FibonacciAdder (num):
    step_list = [0,1]
    index = 0
    for i in range (2,num):
        step = step_list[index] + step_list[index+1]
        step_list.append(step)
        index += 1
    
    return sum(step_list)


# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))