#! /usr/bin/python
import random

# We start with no streaks :)
numberOfStreaks = 0

# We set up a big sample size
for experimentNumber in range(10000):
    # We flip a coin 100 times using a random function and add the result to the list. 1 is for heads, 0 is for tails
    flips = [random.randint(0, 1) for _ in range(100)]
    i = 0
    while i < len(flips):
        # We check the list with a step of 6 coin flips to see if we have a streak of any, heads or tails
        streak = flips[i:i+6]
        if streak == [1,1,1,1,1,1] or streak == [0,0,0,0,0,0]:
            # If we find a streak, we increase the number of streaks
            numberOfStreaks += 1
            # We move to the next set to not count overlapping streaks
            i += 6
        else:
            i += 1   

print('Chance of streak: %s%%' % (numberOfStreaks / 100))    