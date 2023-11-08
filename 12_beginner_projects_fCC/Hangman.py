import random
import string
from Hangman_words import words
#print(words)

def find_valid(words):
    valid_word=random.choice(words)
    while '-' in valid_word or ' ' in valid_word:
        valid_word=random.choice(words)

    return valid_word

def hangman():
    word = find_valid(words)
    word_letters = set(word) #Letters in word
    alphabet = set(string.ascii_lowercase) #Set of all characters in lowercase
    used_letter = set() #Set of letters used
    print(word)
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You\'ve already used : ', ' '.join(used_letter))
        progress = [letter if letter in used_letter else '-' for letter in word]
        print('Current progress :', ''.join(progress))
        print('Lives left :', lives)

        get_input = input('Guess a letter : ')
        if get_input in alphabet - used_letter:
            used_letter.add(get_input)
            if get_input in word_letters:
                word_letters.remove(get_input)
            else:
                lives=lives - 1
        elif get_input in used_letter:
            print('You\'ve already used that letter')
        else:
            print('Invalid input')

        if (len(word_letters) == 0):
            print (f'You guessed "{word}" correctly !')

hangman()