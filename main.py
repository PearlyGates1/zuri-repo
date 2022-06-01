import random

def play():
    possible_action = ['R', 'P', 'S']
    computer = random.choice(possible_action)
    player = input('''Pick a weapon: 'R' for rock, 'P' for paper, 'S' for scissors ''').capitalize()

    while player not in possible_action:
        player = input('''Invalid input, try again: Pick a weapon: 'R' for rock, 'P' for paper, 'S' for scissors ''').upper()

    if player == computer:
        print(f'player ({player}) : CPU ({computer})')
        print('it\'s a tie')
        return play()
        # r > s, s > p, p > r
    elif player == "R":
            if computer == "P":
             print(f'player ({player}) : CPU ({computer})')
            print("You lost!")
            if computer == "S":
                print(f'player ({player}) : CPU ({computer})')
                print("You won!")
        
    elif player == "S":
            if computer == "R":
                print(f'player ({player}) : CPU ({computer})')
                print("You lost!")
            if computer == "P":
                print(f'player ({player}) : CPU ({computer})')
                print("You won!")

    elif player == "P":
        if computer == "S":
            print(f'player ({player}) : CPU ({computer})')
            print("You lost!")
            if computer == "R":
                print(f'player ({player}) : CPU ({computer})')
                print("You won!")
play()