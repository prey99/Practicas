# Write a program to find out how often a streak of six heads
# or a streak of six tails comes up in a randomly generated
# list of heads and tails. Your program breaks up the experiment
# into two parts: the first part generates a list of randomly
# selected 'heads' and 'tails' values, and the second part
# checks if there is a streak in it. Put all of this code
# in a loop that repeats the experiment 10,000 times so
# we can find out what percentage of the coin flips contains
# a streak of six heads or tails in a row.

import random
numberOfStreaks = 0
reps = int(input('How many iterations?: '))
for experimentNumber in range(reps):
    # Code that creates a list of 100 'heads' or 'tails' values.
    acumulado = []
    for i in range(100) :
        flipa = random.randint(0, 1)
        if 0 == flipa :
            acumulado.append('H')
        acumulado.append('T')
    #print(acumulado)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(100) :
        acumuladoSlice = str(acumulado[i:(i+6)])
        #print(acumuladoSlice)
        if "'H', 'H', 'H', 'H', 'H', 'H'" in acumuladoSlice :
            numberOfStreaks += 1
        elif "'T', 'T', 'T', 'T', 'T', 'T'" in acumuladoSlice :
            numberOfStreaks += 1

print('Acumulado: ', numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
 
 