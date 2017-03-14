# Mohammd
#  Program to flip a coin

import random

numFlips = int(input("How many times do you want to flip? "))
count = 0
heads = 0
tails = 0
while count < numFlips:
        flip = random.randint(0,1)
        if flip == 0 :
                flipWord = 'heads'
                heads +=1
        else:
            flipWord = 'tails'
            tails += 1
        count += 1
        print('I flipped, and got', flipWord)
print('\nHeads: ', heads)
print('\nTails: ', tails)
if heads > tails:
        print('\nHeads win')
elif tails > heads:
        print('\nTails win')
else:
        print('\nTie')
