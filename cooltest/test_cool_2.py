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
    return func


def test_select_random_word(func):
    if func() in ["apple", "banana", "cherry", "dog", "elephant", "flower", "giraffe", "hamburger", "icecream", "jacket"]:
        print('Test Word choice pass')
    else:
        print('Test Word choice failed')
    return func


def test_display_word(func):
    word = "apple"
    guessed_letters = ["a", "e"]
    expected_word = "a___e"
    guessed_word = func(word, guessed_letters)
    if expected_word == guessed_word:
        print('Test Display Word pass')
    else:
        print('Test Display Word failed')
    return func

