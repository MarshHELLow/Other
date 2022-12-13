import time

def welcome_bot(bot_name, birth_year):
    print("Hello! My name is " + bot_name + ".")
    print("I was created in " + birth_year + ".")

def welcome_user():
    print("Please, remind me your name.")
    global name
    name = input()
    print(f"What a great name you have, {name}!")
    print(f"\nLet me guess your age, {name}.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is " + str(age) + "; that's a good time to start programming!")

def bot_count():
    print("Now I will prove to you that I can count to any number you want.")
    num = int(input())
    curr = 0
    while curr <= num:
        time.sleep(0.7)
        print(curr)
        curr = curr + 1

def test_1():
    print("What is my name?")
    print("1. John")
    print("2. Overlord")
    print("3. Skynet")
    print("4. Aid")
    user_answer = int(input())
    if user_answer != 3:
        print("Please, try again.\n")
        test_1()
    else:
        print("This is right!\n")

def test_2():
    print("What year was I created?")
    print("1. 2020")
    print("2. 1994")
    print("3. 2076")
    print("4. 2022")
    user_answer = int(input())
    if user_answer == 4:
        print("This is right!\n")
    elif user_answer == 3:
        print("No, this year is in the future. Please, try again.\n")
        test_2()
    else:
        print("Please, try again.\n")
        test_2()

def main():
    welcome_bot("Skynet", "2022")
    welcome_user()
    bot_count()
    print(f"\nPlease answer me a couple of questions {name}.")
    test_1()
    test_2()
    print("Congratulations, have a nice day!")

main()




