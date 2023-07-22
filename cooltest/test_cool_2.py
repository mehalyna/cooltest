import random

def test_play_rock_paper_scissors(func):
    def wrapper(player_choice):
        player_choices = {'r':'rock', 'p':'paper', 's':'scissors'}
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Player's choice: {player_choices[player_choice]}")
        print(f"Computer's choice: {computer_choice}")
        result = func(player_choice)
        return result
    return wrapper