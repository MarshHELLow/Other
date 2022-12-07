import random
print("H A N G M A N")
words_base = ["python", "java", "swift", "javascript"]
word_game = random.choice(words_base)
word_secret = "-" * len(word_game)
letters_view = set()
health_point = 8

while health_point != 0:
    print(word_secret)
    player_letter = input("Input a letter: ")
    if player_letter not in word_game:
        print("That letter doesn't appear in the word.")
        health_point -= 1
    elif player_letter in word_game:
        letters_view.update(player_letter)
        word_secret[word_game.index(player_letter)] = player_letter

print("Thanks for playing!")
