
try:
    f = open('orders.txt','r')
    print ('\nReading previous orders.')
    filecontent = f.read()
    print (filecontent)
except:
    print ('\nPrevious orders not found.')

complete = False
while complete == False:
    try:
        selection = int(input('\nChoose from the following menu items:\n1.\tadd new order\n2.\tlist orders\n3.\texit\n> '))
    except:
        print ('\nThat is not a valid input')
        
    if selection == 1:
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

    elif selection == 2:
        with open ('orders.txt', 'r') as orders:
            for line in orders.readlines():
                a,b,c,d = line.strip().split('|')
                read_orders = (f'{a},\t\t{b} Burger(s), {c} Fries, {d} Cokes')
                print (read_orders)
    elif selection == 3:
        print ('\nEnjoy your meal')
        complete = True
    else:
        print ('\nPlease choose either 1, 2, or 3')