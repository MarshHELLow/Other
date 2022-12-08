import random

health_point = 8
words = ["python", "java", "swift", "javascript"]
answer = list(random.choice(words))
secret_word = list("-" * len(answer))
set_letters = set(answer)
print("H A N G M A N")

while health_point != 0 and secret_word != answer:
    user_letter = input(f"\n{''.join(secret_word)}\nInput a letter:")

    if user_letter in secret_word:
        print('No improvements')
        health_point -= 1

    elif user_letter in set_letters:
        for i in range(len(answer)):
            if answer[i] == user_letter:
                secret_word[i] = user_letter
    else:
        print("That letter doesn't appear in the word.")
        health_point -= 1

print("\nYou guessed the word!\nYou survived!" if secret_word == answer else "You lost!")
