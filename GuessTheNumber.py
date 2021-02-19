# Guess the number game

import random

print('Hello, What is your name?')
name = input()
print('Welcome '+ name + '. I am guessing an number from 1 to 20, can you find it?')
somenumber = random.randint(1, 20)

# print ('Hint:'+str(somenumber))

for guesstaken in range (1,7):
    guessnumber = int(input())
    if guessnumber > somenumber:
        print('Its too high')
    elif guessnumber < somenumber:
        print('Its too low')
    else:
        break

if guessnumber == somenumber:
    print('You are right! its ' + str(somenumber) + '. you guessed it in '+ str(guesstaken) + ' guesses!')
else:
    print('you reached the limit. The number is '+ str(somenumber))