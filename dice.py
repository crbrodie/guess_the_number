from random import randint as r

print('Thanks for trying out my random number gen... I mean dice game!')
print()
dice_size = int(input('Pick a dice size: '))
question = input(f'Roll {dice_size} sided dice? (y/n): ')
if question == 'n':
    print('Come back soon!') 

while question[0] == 'y':
    random_num = r(1,dice_size)
    print('Clack Clack Clack...')
    print(random_num)
    question2 = input(f'Roll {dice_size} sided dice? (y/n or q to quit): ')
    if question2[0] == 'n':
        question = question2
    elif question2[0] == 'y':
        question = question2
    elif question2[0] == 'q':
        print('Come back soon!') 
        break
    else:
        question2 = 'n'
        while question2 == 'n':
            question2 = input(f'Roll {dice_size} sided dice? (y/n or q to quit): ')
            if question2 == 'y':
                question2 = question

    while question[0] == 'n':
        dice_size = int(input('Pick a new dice size: '))
        question2 = input(f'Roll {dice_size} sided dice? (y/n or q to quit): ')
        if question2[0] == 'n':
            question = question2
        elif question2[0] == 'y':
            question = question2
        elif question2[0] == 'q':
           print('Come back soon!') 
           break
        else:
            question2 = 'n'
            while question2 == 'n':
                question2 = input(f'Roll {dice_size} sided dice? (y/n or q to quit): ')
                if question2 == 'y':
                    question2 = question
    