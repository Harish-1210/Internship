username = input("Enter your username: ")
menu = "sign in / sign up"
correct_username = "jacksparrow"

if username == correct_username:
    print("1. Correct")
    print("2. Wrong")
    choice = int(input("Enter the choice (1-2): "))
    if choice == 1:
        print("Login successful!")
    elif choice == 2:
        print("you marked to be wrong.")
    else:
        print("Invalid choice")
else:
    print("forgot password.")
    print("Please", menu)
