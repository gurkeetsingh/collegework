import random
#rand=random.choice(['stone','paper','scissor'])

print('CHOOSE FROM \nstone\npaper\nscissor\n')
#u=int(input('enter your choice'))
win = 0

for i in range(1,10):
    u=(input('enter your choice: '))
    rand=random.choice(['stone','paper','scissor'])
    print(f'the comp choose {rand}')
    if(u==rand):
        print('its a tie')
    elif (u=='stone'):
        if(rand=='paper'):
            print('you lose')
        elif(rand=='scissor'):
            print('you win')
    elif (u=='paper'):
        if(rand=='scissor'):
            print('you lose')
        elif(rand=='stone'):
            print('you won')
    elif (u=='scissor'):
        if(rand=='stone'):
            print("you lose")
        elif(rand=='paper'):
            print("you won")
