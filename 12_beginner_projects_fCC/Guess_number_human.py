import random

def comp_guess(y):
    lwr = 1
    upr = y
    feedback = ''
    while feedback != 'c':
        guess = random.randint(lwr, upr)
        feedback = input(f"Is {guess} too (H)igh, too (L)ow, or (C)orrect").lower()
        if feedback == 'h':
            upr = guess-1
        elif feedback == 'l':
            lwr = guess+1
        elif feedback == 'c':
            print(f"{guess} is correct !")

comp_guess(9)