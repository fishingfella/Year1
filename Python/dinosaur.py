def validate(choice, question):
    while choice != "yes" and choice != "no" and choice.strip():
        print("Enter a valid option")
        choice = str(input(f"\n{question}\n"))
    
    return choice

choice = (str(input("Does the animal have horns?\n"))).lower()
choice = validate(choice, "Does the animal have horns?")
if choice == "yes":
    print("Safe")
elif choice == "no":
    choice = (str(input("Does the animal have boney plates?\n"))).lower()
    choice = validate(choice, "Does the animal have boney plates?")
    if choice == "yes":
        print("Safe")
    elif choice == "no":
        choice = (str(input("Does it have canines?\n"))).lower()
        choice = validate(choice, "Does it have canines?")
        if choice == "no":
            choice = (str(input("Can it fly?"))).lower()
            choice = validate(choice, "Can it fly?\n")
            if choice == "yes":
                print("Danger")
            elif choice == "no":
                print("Safe")
        elif choice == "yes":
            print("Danger")
