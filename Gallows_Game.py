import random

health_point = 8
print("H A N G M A N\n")
words_base = ["python", "java", "swift", "javascript"]
answer = random.choice(words_base)
secret_word = list("-" * len(answer))

while health_point != 0:
    print(''.join(secret_word))
    player_letter = input("Input a letter: ")
    if player_letter in answer:
        for i in range(len(answer)):
            if answer[i] == player_letter:
                secret_word[i] = player_letter
    else:
        print("That letter doesn't appear in the word.")
    health_point -= 1

print("Thanks for playing!")
