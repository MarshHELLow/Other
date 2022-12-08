import random

health_point = 8
words = ["python", "java", "swift", "javascript"]
answer = list(random.choice(words))
secret_word = list("-" * len(answer))
set_letters = set(answer)
set_user_letters = set()
print("H A N G M A N")

def check():
    global user_letter
    if len(user_letter) != 1:
        print("Please, input a single letter.")
        game()
    elif user_letter.islower() == False:
        print("Please, enter a lowercase letter from the English alphabet.")
        game()
    elif user_letter in set_user_letters:
        print("You've already guessed this letter.")
        game()

def game():
    global health_point
    global user_letter
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
            health_point -= 1

game()
if secret_word.count('-') > 0:
    print("\nYou lost!")
else:
    print(f"\nYou guessed the word {''.join(answer)}!\nYou survived!")

