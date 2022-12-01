import string

print("How many pencils would you like to use:")

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
right_count()


print("Who will be the first (John, Jack):")

def right_name():
    global name
    name = input()
    if name != "John" and name != "Jack":
        print("Choose between John and Jack")
        right_name()
right_name()

print("|" * count)
while count > 0:
    if name == "John":
        print(f"{name}'s turn:")
        name = "Jack"
    else:
        print(f"{name}'s turn:")
        name = "John"

    def right_count_user():
        global count_user
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
    right_count_user()

    count = count - count_user
    print("|" * count)

    if count == 0:
        if name == "John":
            print(f"{name} won!")
        else:
            name = "Jack"
            print(f"{name}' won!")



