import random
a = 0
i = ['rock', 'paper', 'scissors']
while (a == 0):
        p = str(input('Instruction: input rock, paper or scissors '))
        if (p == i[0] or p == i[1] or p == i[2]):
            a = 1    
        else:
            print('pls read instruction one more time')
if p == i[0]:
    print('u have choosen rock')  
elif p == i[1]:
    print('u have choosen paper') 
elif p == i[2]:
    print('u have choosen scissors')  
c = i[random.randint(0, 2)]
if c == i[0]:
    print('enemy has choosen rock') 
elif c == i[1]:
    print('enemy has choosen paper')
elif c == i[2]:
    print('enemy has choosen scissors')
if p == c:
    print('draw')
elif  p == i[0] and c == i[2]:
    print('u have won')
elif p == i[1] and c == i[0]:
    print('u have won')
elif p == i[2] and c == i[1]:
    print('u have won')
else:
    print('u have lost')