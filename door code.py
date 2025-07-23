door=input("door is the open(yes/no):")
if door=="yes":
    print("1.quick wash")
    print("2.heavy wash")
    print("3.spin wash")
    choice=int(input("enter the choice(1-3):"))
    if choice==1:
       print("quick wash")
    elif choice==2:
       print("heavy wash")
    elif choice==3:
       print("spin started")
    else:
       print("program choice")
else:
     print("please open the door")
