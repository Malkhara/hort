# Hedge's idea 
#  Program to flip a coin

import random

flip = random.randint(0,1)

if (flip ==0):
    flipWord = 'heads'
else:
    flipWord = 'tails'

print('I flipped, and got', flipWord)

