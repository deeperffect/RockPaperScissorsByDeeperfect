import random
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')
if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid Input. Try again...')

random_number = random.randint(1, 3)
computer_move = ''
if random_number == 1:
    computer_move = rock
    print('The computer chose Rock')
elif random_number == 2:
    computer_move = paper
    print('The computer chose Paper')
else:
    computer_move = scissors
    print('The computer chose Scissors')

if (player_move == rock and computer_move == rock) or (player_move == paper and computer_move == paper) or (player_move == scissors and computer_move == scissors):
    print("It's a draw")
elif (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or (player_move == scissors and computer_move == paper):
    print('You win!')
else:
    print('You lose!')