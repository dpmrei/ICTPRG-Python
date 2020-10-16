with open("logins2.txt", "r") as loginfile:
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))

    for line in loginfile:
        uname, upassword = line.strip().split(":")
        if username == uname and password == upassword:
            print("Access granted!")
            break
    else:
        print("Access denied.")