def right_count():
    global count
    count = input()
    if count.isdigit() == False:
        print("The number of pencils should be numeric")
        right_count()
    elif int(count) == 0:
        print("The number of pencils should be positive")
        right_count()
    elif int(count) < 0:
        print("The number of pencils should be numeric")
        right_count()
    count = int(count)

def right_name():
    global name
    name = input()
    if name != "John" and name != "Jack":
        print("Choose between John and Jack")
        right_name()

def right_count_user():
    global count_user
    global count
    if name == "Jack":
        count_user = input()
        if count_user.isdigit() == False:
            print("Possible values: '1', '2' or '3'")
            right_count_user()
        if int(count_user) != 1 and int(count_user) != 2 and int(count_user) != 3:
            print("Possible values: '1', '2' or '3'")
            right_count_user()
        if int(count_user) > count:
            print("Too many pencils were taken")
            right_count_user()
        count_user = int(count_user)
    elif name == "John":
        if count % 4 == 0:
            count_user = 3
        elif count % 4 == 3:
            count_user = 2
        elif count % 4 == 2:
            count_user = 1
        elif count % 4 == 1:
            count_user = 1
        else:
            count_user = 1
        print(count_user)
print("How many pencils would you like to use:")
right_count()
print("Who will be the first (John, Jack):")
right_name()
print("|" * count)
while count > 0:
    if name == "Jack":
        print(f"{name}'s turn!")
        name = "John"
    else:
        print(f"{name}'s turn:")
        name = "Jack"
    right_count_user()

    count = count - count_user
    print("|" * count)

    if count == 0:
        if name == "Jack":
            print(f"{name} won!")
        else:
            name = "John"
            print(f"{name}' won!")



