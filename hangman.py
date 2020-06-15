import random
from string import ascii_lowercase

print("H A N G M A N\n")

while input('Type "play" to play the game, "exit" to quit:') != "play":
    continue

word_options = ['python', 'java', 'kotlin', 'javascript']
tries = 8
word = random.choice(word_options)
hidden_word = "-" * len(word)
chars_set = set(word)

guessed_chars_set = set()

while tries > 0:
    if hidden_word == word:
        print(f"You guessed the word {word}!")
        print("You survived!")
        break

    print("\n" + hidden_word)
    char = input("Input a letter: ")

    if len(char) != 1:
        print("You should input a single letter")
        continue

    if char not in ascii_lowercase:
        print("It is not an ASCII lowercase letter")
        continue

    if char in guessed_chars_set:
        print("You already typed this letter")
        continue

    guessed_chars_set.add(char)

    if char in chars_set:
        for j in range(len(word)):
            if word[j] == char:
                hidden_word = hidden_word[:j] + char + hidden_word[j + 1:]
    else:
        print("No such letter in the word")
        tries -= 1
else:
    print("You are hanged!")