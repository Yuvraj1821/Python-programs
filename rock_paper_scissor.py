import random

def play_with_com():
    player = input("What's Your choice? from 'r' for rock, 'p' for paper, 's' for scissor : ")
    com = random.choice(['r', 'p', 's'])

    if player == com:
        print('tie!')
    elif rps(player, com):
        print('You Won!')
    else:
        print('You lost')


def play_with_player():
    player1 = input("Player 1 | 'r' for rock, 'p' for paper, 's' for scissor : ")
    player2 = input("PLayer 2 | 'r' for rock, 'p' for paper, 's' for scissor : ")

    if player1 == player2:
        print('tie!')
    elif rps(player1, player2):
        print('Player 1 Won!')
    else:
        print('Player 2 Won!')


def rps(opponent1, opponent2):
    if (opponent1 == 'r' and opponent2 == 's') or (opponent1 == 's' and opponent2 == 'p') \
            or (opponent1 == 'p' and opponent2 == 'r'):
        return True


choice = input("\t\t\t\t\t\t\t\t\t 1 for computer | 2 for player : ")
if(choice == 1):
    play_with_com()
else:
    play_with_player()