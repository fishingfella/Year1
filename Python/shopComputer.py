def findByName():
    shopContacts = open("shopContacts.csv", "r")
    line = shopContacts.readline()
    found = False

    name = str(input("Enter a name: "))
    while not name.split():
        print("\nEnter a value")
        name = str(input("\nEnter a name: "))

    while (line):
        data = line.split(",")
        fullName = data[0].split()
        if data[0].lower() == name.lower() or fullName[0].lower() == name.lower() or fullName[1].lower() == name.lower():
            print(f"Name: {data[0]}\nAddress: {data[1]}\nCity: {data[2]}\nPhone Number: {data[3]}")
            found = True

        line = shopContacts.readline()

    if found != True:
        print("Name not found.")
    
    shopContacts.close()

def findByCity():
    shopContacts = open("shopContacts.csv", "r")
    line = shopContacts.readline()
    found = False

    city = str(input("Enter a city: "))
    while not city.split():
        print("\nEnter a value")
        city = str(input("Enter a city: "))

    while (line):
        data = line.split(",")
        if data[2].lower() == city.lower():
            print(f"Name: {data[0]}\nAddress: {data[1]}\nCity: {data[2]}\nPhone Number: {data[3]}")
            found = True

        line = shopContacts.readline()

    if found != True:
        print("City not found.")
    
    shopContacts.close()

def findByNumber():
    shopContacts = open("shopContacts.csv", "r")
    line = shopContacts.readline()
    found = False

    number = str(input("Enter a Phone Number: "))
    while not number.split():
        print("\nEnter a value")
        number = str(input("Enter a Phone Number: "))

    while (line):
        data = line.split(",")
        if data[3] == number:
            print(f"Name: {data[0]}\nAddress: {data[1]}\nCity: {data[2]}\nPhone Number: {data[3]}")
            found = True

        line = shopContacts.readline()

    if found != True:
        print("Phone Number not found.")
    
    shopContacts.close()

def createContact():
    shopContacts = open("shopContacts.csv", "a")

    name = str(input("Enter a Name: "))
    while not name.split():
        print("Field Empty.")
        name = str(input("\nEnter a Name: "))
    name = name.replace(",", "")

    address = str(input("Enter a Address: "))
    while not address.split():
        print("Field Empty.")
        address = str(input("\nEnter a Address: "))
    address = address.replace(",", "")

    city = str(input("Enter a City: "))
    while not city.split():
        print("Field Empty.")
        city = str(input("Enter a City: "))
    city = city.replace(",", "")

    phoneNumber = str(input("Enter a Phone Number: "))
    while not phoneNumber.split():
        print("Field Empty.")
        phoneNumber = str(input("Enter a Phone Number: "))
    phoneNumber = phoneNumber.replace(",", "")

    shopContacts.write(f"\n{name},{address},{city},{phoneNumber}")

    shopContacts.close()


done = False
while done != True:
    print("1: Find by Name\n2: Find by City\n3: Find by Phone Number\n4: Create a new contact\n5: Exit the program")
    try:
        option = int(input("\nSelect an option: "))
    except ValueError:
        print("Please enter a number.\n")

    while option <= 1 and option >= 5:
        print("Please enter a correct option.\n")
        try:
            option = int(input("\nSelect an option: "))
        except ValueError:
            print("Please enter a number.\n")

    if option == 1:
        findByName()
    elif option == 2:
        findByCity()
    elif option == 3:
        findByNumber()
    elif option == 4:
        createContact()
    elif option == 5:
        done = True