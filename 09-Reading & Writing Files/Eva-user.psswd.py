with open ('logins.txt', 'w') as source:
    source.write('user0:password10\n')
    source.write('user1:password9\n')
    source.write('user2:password8\n')
    source.write('user3:password7\n')
    source.write('user4:password6\n')
    source.write('user5:password5\n')





username = input('Username? : ')
password = input('Password? : ')
File = open('logins.txt', 'r')
for line in File.readlines():
    usr, psswd = line.strip().split(':')

    if username == usr and password == psswd:
        print('Access granted')
    else:
        print('Access denied')