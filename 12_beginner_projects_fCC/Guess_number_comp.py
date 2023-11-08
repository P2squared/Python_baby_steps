import random

def guesser(x):
    rand_num = random.randint(1, x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f"Guess a number between 1 and {x}"))
        if guess < rand_num:
            print("Too low, guess again !")
        elif guess > rand_num:
            print("Too high, guess again !")

    print(f"You guessed {rand_num} correctly !")

guesser(8)
