import random

#roll = random.randint(1,6)

for i in range(1, 11):
    roll = random.randint(1,6)
    guess = int(input('Guess a number on the die:\n'))
    if guess == roll:
        print('Correct')
    else:
        print('Wrong Try again')
    
