dictionary  = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
sentence = input('\n[+]  Please input a sentence.  Longer is preferable:\t').lower()

for key in dictionary:
    for i in sentence:
        count = sentence.count(key)
        dictionary[key] = count
    print (f"\nThere are {count} {key}'s")
    
print ()
print (dictionary)
print ()
for k, v in dictionary.items():
    print(k, ' : ', v)
print ()