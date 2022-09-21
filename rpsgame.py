import random as rd

human_turn = input('(R)ock, (P)aper , (S)cissors : ')
computer_turn = rd.choice(["Rock","Paper","Scissors"])
print("computer chooses : " + computer_turn)
if human_turn == computer_turn:
        print('Draw!')
elif human_turn == 'Rock' and computer_turn == 'Scissors':
    print('Human Wins')
elif human_turn == 'Paper' and computer_turn == 'Rock':
    print('Human Wins')
elif human_turn == 'Scisors' and computer_turn == 'Paper':
    print('Human Wins') 
else:
    print('Computer Wins!')
    
