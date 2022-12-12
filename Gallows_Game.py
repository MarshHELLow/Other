import random

health_point = 8
words = ["python", "java", "swift", "javascript", "programming", "jetbrains", "github", "freedom", "world"]
count_won = 0
count_lost = 0

def start_menu():
    global health_point, start_user, secret_word, set_letters, set_user_letters, answer
    health_point = 8
    answer = list(random.choice(words))
    secret_word = list("-" * len(answer))
    set_letters = set(answer)
    set_user_letters = set()
    print("H A N G M A N")
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    start_user = 0
    while start_user != "play":
        start_user = input()
        if start_user == "results":
            print(f"You won: {count_won} times.\nYou lost: {count_lost} times.")
            start_menu()
        elif start_user == "exit":
            return 0
    game()

def check():
    global user_letter, set_user_letters
    if len(user_letter) != 1:
        print("Please, input a single letter.")
        game()
    elif user_letter.islower() == False:
        print("Please, enter a lowercase letter from the English alphabet.")
        game()
    elif user_letter in set_user_letters:
        print("You've already guessed this letter.")
        game()

def win():
    global count_lost, count_won
    if secret_word.count('-') > 0:
        count_lost += 1
        print("\nYou lost!")
        start_menu()
    else:
        count_won += 1
        print(f"\nYou guessed the word {''.join(answer)}!\nYou survived!")
        start_menu()

def game():
    global health_point, user_letter
    while health_point > 0 and secret_word != answer:
        user_letter = input(f"\n{''.join(secret_word)}\nInput a letter:")
        check()
        if user_letter in set_letters:
            set_user_letters.update(user_letter)
            for i in range(len(answer)):
                if answer[i] == user_letter:
                    secret_word[i] = user_letter
        else:
            print("That letter doesn't appear in the word.")
            set_user_letters.update(user_letter)
            health_point -= 1
    win()

def main():
    start_menu()
main()
