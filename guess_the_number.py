from random import randint as r
e = 'easy'
m = 'medium'
h = 'hard'

difficulty = input('I want to play a game. Choose difficulty now. (easy/medium/hard:  ').lower()
if difficulty[0] == 'e':
    rand = r(1,10)
    difficulty ='Easy'
    lives = 5
    n = 10
elif difficulty[0] == 'm':
    rand = r(1,100)
    difficulty = 'Medium'
    lives = 10
    n = 100
elif difficulty[0] == 'h':
    rand = r(1,1000)
    difficulty = 'Hard'
    lives = 10
    n = 1000
else:
    difficulty = input('Thats..not one of the three choices. Alright lets try this one more time! Choose difficulty now. (easy/medium/hard):  ').lower()
    if difficulty[0] == 'e':
        rand = r(1,10)
        difficulty ='Easy'
        lives = 5
        n = 10
    elif difficulty[0] == 'm':
        rand = r(1,100)
        difficulty = 'Medium'
        lives = 10
        n = 100
    elif difficulty[0] == 'h':
        rand = r(1,1000)
        difficulty = 'Hard'
        lives = 10
        n = 1000
    else:
        print("Bless your heart, maybe this game isn't for you...")
        quit('BYEEEEEE')
print(f"Okay! {difficulty} it is!! Guess a number between 1 and {n}. You'll start with {lives} lives, dont waste 'em!")    
user_guess = int(input(f"I'm thinking of a number, can you guess what it is ({lives} lives)?  "))

if user_guess == rand:
    print(f'Wow.. good job, it was {rand}! First try, too!')
   
while rand != user_guess:
    if lives >= 0:
        if rand > user_guess:
            lives = lives - 1
            user_guess = int(input(f'Try higher ({lives} lives):  '))
            

        elif rand < user_guess:
            lives = lives - 1
            user_guess = int(input(f'Try lower ({lives} lives):  '))
           
if user_guess == rand:
    print(f'Wow.. good job, it was {rand}! And you still have {lives} lives!')
if lives < 0:
    print('Oh no, you ran out of lives! Better luck next time!')
