import random
from title import title
from random_word import RandomWords
from os import system, name
from display import displayHangman
import json
import time

with open("words.json") as f:
    data = json.load(f)

def clear():
    if name == "nt":
        _ = system("cls")
    
    else:
        _ = system("clear")

def getWord():
    wlist = []
    for word in data["words"]:
        wlist.append(word["word"])
    word = random.choice(wlist)
    return word.upper()


def play(word):
    wordCompletion = "-" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    print(title)
    print(displayHangman(tries))
    print(wordCompletion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Enter guess here: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("You already guessed the letter", guess)
                time.sleep(2)
                clear()
                print(title)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessedLetters.append(guess)
                time.sleep(2)
                clear()
                print(title)
            else:
                print(f'{guess} is in the word!')
                time.sleep(2)
                clear()
                print(title)

                guessedLetters.append(guess)
                wordAsList = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                wordCompletion = "".join(wordAsList)
                if "_" not in wordCompletion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print(f"You already guessed the word {guess}")
                time.sleep(2)
                clear()
                print(title)
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessedWords.append(guess)
                time.sleep(2)
                clear()
                print(title)
            else:
                guessed = True
                wordCompletion = word
        else:
            print(f"{guess} is not a valid guess.")
            time.sleep(2)
            clear()
            print(title)
        print(displayHangman(tries))
        print(wordCompletion)
        print("\n")
    if guessed:
        print("You guessed the word!")
        time.sleep(2)
        clear()
        print(title)
    else:
        print(f"Out of tries. The word was {word}. Maybe next time!")
        time.sleep(2)
        clear()
        print(title)

def main():
    word = getWord()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        clear()
        word = getWord()
        play(word)
    clear()

if __name__ == "__main__":
    main()
