
grade = int(input('What was your grade? '))

if grade < 50:
    print ('You suck.... and you fail')

elif grade >= 50 and grade <= 69:
    print ('You will receive a Pass')

elif grade >= 70 and grade <= 79:
    print ('You will receive a Credit')

elif grade >= 80 and grade <= 89:
    print ('You will receive a Distinction')

elif grade >= 90 and grade <= 100:
    print ('You will receive a High Distinction')

else:
    print ('You probably failed if you think you got over 100')

    