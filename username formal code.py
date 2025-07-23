username = "jacksparrow"
password = "jack@123"
a = input("Enter username: ")
b = input("Enter password: ")
if a == username and b == password:
    print("Welcome to you")
elif a == username and b != password:
    print("Correct username but forgot password")
elif a != username and b == password:
    print("Correct password but forgot username")
elif a == "jacksparrow":
    print("Username entered:", a)
elif b == "jack":
    print("Password entered:", b)
else:
    print("Invalid data")

