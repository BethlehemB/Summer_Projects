user_name = input("What is your name? ")
print("Welcome", user_name, "! Have fun and make good decisions :)\n")

answer = input("You are at end of a dirt road you can either go left or right ").lower()

if answer == "left":
    answer = input("Your now in a wooded area and you have across a swamp, would you like to swim across it or walk around it?\n").lower()

    if answer == "swim":
        answer1 = input("Oh no an alligator! Will you throw something at it or swim faster? Please type in throw or faster: \n").lower()
        if answer1 == "throw":
            print("You threw a chicken at the alligator and evaded the attack but died of hunger the next day :( Sorry!)")
        elif answer1 == "faster": 
            print("You weren't fast enough and got gobbled up :(")
        else:
            print("Not a valid option you die!")

    elif answer == "walk":
        print("You walk for days on end and fall to your knees at that moment of weakness a gorilla appeared and ripped you apart :(")
    else:
        print("Not a valid option you die!")



elif answer == "right":
    answer = input("Theres a bridge and it looks kind of wobbly will you cross it or turn back. Please either type cross or back \n").lower()

    if answer == "back":
            print("Game Master felt as if you were to scared to journey forward and killed you!")
    elif answer == "cross":
        answer = input("You come across a stranger they could have some valuable info? Would you like to talk to them? (yes/no) ").lower()

        if answer == "yes":
            print("She takes a liking to you after you commented about her eyes and gave you some gold! YOU WIN!!!")
        
        elif answer == "no":
            print("She was a siren and offended you ignored her she stole your soul and you died!")
        
        else:
            print("Not a valid option you die!")

    else:
        print("Not a valid option you die!")


else:
    print("Not a valid option you die!")
