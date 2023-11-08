import random
import string
from Hangman_words import words
# print(words)

def get_valid(wor):
    secr = random.choice(wor)
    while '-' in secr or ' ' in secr:
        secr = random.choice(wor)

    return secr

def hangman(get_valid):
    alphabet = set(string.ascii_lowercase)
    secret = get_valid(words)
    print(secret)
    word_letters = set(secret)
    used_letters = set()
    lives = 6

    while lives > 0 and len(word_letters) > 0 :
        print(f'You\'ve already used ',' '.join(used_letters), ' letters.')
        print(f'You have {lives} attempts left')
        progress = [letter if letter in used_letters else '-' for letter in secret]
        print('Current progress :', ''.join(progress))

        get_inp = input('Guess a letter')
        if get_inp in alphabet - used_letters:
            used_letters.add(get_inp)
            if get_inp in word_letters:
                word_letters.remove(get_inp)
            else:
                lives = lives - 1
        elif get_inp in used_letters:
            print(f'You\'ve already guessed {get_inp}')
        else:
            print('Invalid input')

        if (len(word_letters) == 0):
            print (f'You guessed "{secret}" correctly !')


hangman(get_valid)
