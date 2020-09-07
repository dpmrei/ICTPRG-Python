



sentence = input('\n[+]  Please enter a sentence:\n\n')
segment = input('\n[+]  Please enter one word from within your sentence:\n\n')
  
if len(sentence) <= len(segment):
    print ("\nI'm sorry, but the length of your segment was longer than your actual sentence.\nBye for now.\n")

result = sentence.find(segment)

print (f'\n[+]  Your segment was found at index {result}.\n')

if (sentence.find(segment)) == -1:
    print ('Your segement was not found within the sentence.\n')

