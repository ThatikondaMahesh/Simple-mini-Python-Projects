#program to guess
import random
def guess(x):
    chosen_number=random.randint(1,x)
    guess=0
    print(chosen_number)
    while(guess!=chosen_number):
        guess=int(input(f'guess the b/w 1 to {x}'))
        if guess > chosen_number:
            print('sorry invalid guess TOO high ')
        elif(guess<chosen_number):
            print('sorry invalid number low ')
    print(f'yay ! u guessed the correct number{guess}')
            


guess(90) 