import random

#Check for correct input of the initial number of pencils
def right_count():
    global count
    count = input()
    if count.isdigit() == False:
        print("The number of pencils should be numeric")
        right_count()
    elif int(count) == 0:
        print('The number of pencils must not be "zero"')
        right_count()
    elif int(count) < 0:
        print("The number of pencils should be positive")
        right_count()
    count = int(count)

#Checking for the correct input of the name of the first player
def right_name():
    global name
    name = input()
    if name != "User" and name != "Bot":
        print("Choose between User and Bot")
        right_name()

#Logic of the main game process
def game():
    global count_user
    global count
    if name == "Bot":
        count_user = input()
        if count_user.isdigit() == False:
            print("Possible values: '1', '2' or '3'")
            game()
        if int(count_user) != 1 and int(count_user) != 2 and int(count_user) != 3:
            print("Possible values: '1', '2' or '3'")
            game()
        if int(count_user) > count:
            print("Too many pencils were taken")
            game()
        count_user = int(count_user)
    elif name == "User":
        if count % 4 == 0:
            count_user = 3
        elif count % 4 == 3:
            count_user = 2
        elif count % 4 == 2 or count % 4 == 1:
            count_user = 1
        else:
            random.seed(count)
            count_user = random.randint(1, 3)
        print(count_user)

#Checking for a winner
def win():
    global name
    if count == 0:
        if name == "Bot":
            print(f"The {name} wins!")
        else:
            name = "User"
            print(f"{name}' won!")

#Execution of the main program
print("How many pencils would you like to use:")
right_count()
print("Who will be the first (User, Bot):")
right_name()
print("|" * count)
while count > 0:
    if name == "Bot":
        print(f"{name}'s turn!")
        name = "User"
    else:
        print(f"{name}'s turn:")
        name = "Bot"
    game()
    count = count - count_user
    print("Remaining pencils on the playing field:")
    print("|" * count)
    win()




