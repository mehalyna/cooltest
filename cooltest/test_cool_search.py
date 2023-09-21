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
    actual_list = func(cell, grid)
    if actual_list:
        print('Test Is Valid Pass')
    else:
        print('Test Is Valid Failed')
    return func


def get_neighbors(func):
    grid = [
    ['S', ' ', ' ', ' ', ' '],
    ['X', 'X', ' ', ' ', 'E'],
    [' ', ' ', 'X', ' ', ' '],
    ['X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ']
    ]
    cell = (0, 2) #(row, col)
    expected_neighbors = [(1, 2), (0, 1), (0, 3)]
    actual_neighbors = func(cell, grid)
    if expected_neighbors == actual_neighbors:
        print('Test Is Valid Pass')
    else:
        print('Test Is Valid Failed')
    return func

