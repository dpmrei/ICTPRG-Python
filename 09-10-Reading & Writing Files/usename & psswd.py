
with open ('logins.txt', 'w') as source:
    source.write('user0:password10\n')
    source.write('user1:password9\n')
    source.write('user2:password8\n')
    source.write('user3:password7\n')
    source.write('user4:password6\n')
    source.write('user5:password5\n')

username = input('[+]  Please enter your username:\t')
password = input('[+]  Please enter your password:\t')

with open ('logins.txt', 'r') as checklist:
    for line in checklist.readlines():
        u, p = line.strip().split(':')
        if username == u and password == p:
            print (f'\nUsername? : {username}\tPassword? : {password} - \tAccess Granted!\n')
            break

    else:
        print ('\nAccess Denied!\n')
        
