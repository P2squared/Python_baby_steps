import random

def compu() :
    pc = random.choice(['r', 'p', 's'])
    plr = input('Enter input (r)ock, (p)aper, or (s)cissors')
    print(f'PC chose {pc}, you chose {plr}')

    if plr == pc:
        return 'Tie'

    if win(plr, pc):
        return 'You win'

    return 'You lose'

def win(p1, p2):
    # r>s, s>p, p>r

    if (p1 == 'r' and p2 == 's') or (p1 == 's' and p2 == 'p') or (p1 == 'p' and p2 == 'r'):
        return True

print(compu())
