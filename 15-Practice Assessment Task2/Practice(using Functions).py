

def Check4File():

    try:
        f = open('orders.txt','r')
        print ('\nReading previous orders.')
        filecontent = f.read()
        #print (filecontent)
    except:
        print ('\nPrevious orders not found.')

Check4File()

def Selection():
    while True:
        print ('\nPlease choose from the following:\n1.\tAdd new order\n2.\tList orders\n3.\tExit')
        try:
            selection = int(input('>\t'))
        except:
            print ("Please select either '1', '2', or '3'")
        
        if selection == 1:
            Select_1()
        
        elif selection == 2:
           Read_Orders()

        elif selection == 3:
            print ('\nEnjoy your meal')
            break

def Select_1():
    with open ('orders.txt', 'a') as orders:
            print ('Please select the quantity of each item you wish to order')
            name = input('Firstly, enter your name:\t')
            try:
                burgers = int(input('Burgers:\t'))
                fries = int(input('Fries:\t\t'))
                cokes = int(input('Cokes:\t\t'))
            
                output = (f'{name}|{burgers}|{fries}|{cokes}')
                print (output)
                orders.write(f'{output}\n')
            except:
                print ('\nThat is not a valid input')

def Read_Orders():
    with open ('orders.txt', 'r') as orders:
            for line in orders.readlines():
                a,b,c,d = line.strip().split('|')
                read_orders = (f'{a},\t\t{b} Burger(s), {c} Fries, {d} Cokes')
                print (read_orders)


Selection()
