import random

def test_play_rock_paper_scissors(func):
    player_choice = 'rock'
    computer_choice = 'paper'
    result = func(player_choice, computer_choice)
    if result == "Comp wins":
        print("Test game Pass")
    else:
        print("Test game Failed")
        
    return func

def test_computer_makes_choice(func):
    if func() in {'rock', 'paper', 'scissors'}:
        print('Test Comp choice pass')
    else:
        print('Test Comp choice failed')