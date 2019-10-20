item = []
while True:
    print('press 1 to add item')
    print (' press 2 to find item')
    print (' press 3 to find the total number of items')
    print (' press 4 to exit')
    choice = input(' Enter your Choice; ')
    if choice == 1 :
        item = {}
        item [' Number'] = input ('Enter the item number ')
        item ['Name'] = input(' Enter the name of item ')
        item [' price'] = input (' Enter the Price of item')
        items.append(items)
    elif choice == 2 :
        name = input (' Enter the item name you want to search for :')
        for item in items:
            if item[ 'Name'].lower() == name.lower() :
                print (' ITEM with name' + name + 'found')
                print (item)  