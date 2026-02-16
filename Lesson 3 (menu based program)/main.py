#main menu

while True:
    print("--- Main Menu ---\n 1. List Operations\n 2. Tuple Operations\n 3. Dictionary Operations\n 4. Set Operations\n 5. Exit")
    userinput = int(input("Enter your choice: "))
    #list operations
    if userinput == 1:
        list1 = []
        while True:
            print("--- List Menu ---\n 1. Add Element\n 2. Remove Element\n 3. View List\n 4. Back to main menu")
            listinput = int(input("Enter your choice: "))
            if listinput == 1:
                addinput = input("What would you like to add?")
                list1.append(addinput)
            elif listinput == 2:
                delinput = input("What would you like to delete?")
                list1.remove(delinput)
            elif listinput == 3:
                print(list1)
            elif listinput == 4:
                print("Returning to main menu...")
                break
    elif userinput == 2:
        tuple1 = ()
        while True:
            print("--- Tuple Menu ---\n 1. Create Tuple\n 2. Display Tuple\n 3. Count Element\n 4. Exit")
            tupleinput = int(input("Enter your choice: "))
            if tupleinput == 1:
                tupleadd = input("Please input values with spaces inbetween ")
                tuple1 = tuple(tupleadd.split())
            elif tupleinput == 2:
                print(tuple1)
            elif tupleinput == 3:
                print(len(tuple1))
            elif tupleinput == 4:
                print("Returning to main menu...")
                break    
    elif userinput == 3:
        dict1 = {}
        while True:
            print("--- Dictionary Menu ---\n 1. Add key value pair\n 2. Delete key\n 3. Display Dictionary\n 4. Exit ")
            dictinput = int(input("Enter your choice: "))
            if dictinput == 1:
                keyadd = input("Enter a key: ")
                pairadd = input("Add a pair: ")
                dict1[keyadd] = pairadd
            elif dictinput == 2:
                delkey = input("What key would you like to delete? ")
                del dict1[delkey]
            elif dictinput == 3:
                print(dict1)
            elif dictinput == 4:
                print("Returning to main menu...")
                break
    elif userinput == 4:
        set1 = set()
        while True:
            print("--- Set Menu ---\n 1. Add Element\n 2. Remove Element\n 3. Show set\n 4. Exit")
            setinput = int(input("Enter your choice: "))
            if setinput == 1:
                setadd = input("What would you like to add? ")
                set1.add(setadd)
            elif setinput == 2:
                setrem = input("What would you like to delete? ")
                set1.remove(setrem)
            elif setinput == 3:
                print(set1)
            elif setinput == 4:
                print("Returning to main menu...")
                break
    elif userinput == 5:
        print("Exiting the program...")
        break
    else:
        print("Please enter a valid value!")
            