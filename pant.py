pant = input("Select the pant (yes/no): ")
if pant.lower() == "yes":
    print("1. Blue")
    print("2. Black")
    print("3. Yellow")
    choice = int(input("Select the pant color (1-3): "))
    if choice == 1:
        print("You selected: Blue")
    elif choice == 2:
        print("You selected: Black")
    elif choice == 3:
        print("You selected: Yellow")
    else:
        print("Invalid choice")
else:
    print("No pant color selected")
