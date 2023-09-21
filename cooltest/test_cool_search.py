def test_search_word(func):
    word = "ROCK"
    grid = [['A', 'B', 'C', 'R'], ['E', 'F', 'G', 'O'], ['I', 'J', 'K', 'C'], ['M', 'N', 'O', 'K']]
    
    if func(grid, word):
        print('Test Display Word pass')
    else:
        print('Test Display Word failed')
    return func


def test_find_words(func):
    words = ["ROCK", "IN", "OF"]
    grid = [['A', 'B', 'C', 'R'], ['E', 'F', 'G', 'O'], ['J', 'I', 'K', 'C'], ['M', 'N', 'O', 'K']]
    expected_list = ["ROCK", "IN"]
    actual_list = func(grid, words)
    if expected_list == actual_list:
        print('Test Find Words pass')
    else:
        print('Test Find Words failed')
    return func


def test_is_valid(func):
    grid = [
    ['S', ' ', ' ', ' ', ' '],
    ['X', 'X', ' ', ' ', 'E'],
    [' ', ' ', 'X', ' ', ' '],
    ['X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ']
    ]
    cell = (0, 1)
    expected_list = func(cell, grid)
    if expected_list:
        print('Test Is Valid Pass')
    else:
        print('Test Is Valid Failed')
    return func

