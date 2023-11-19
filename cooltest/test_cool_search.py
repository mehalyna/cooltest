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


def test_find_shortest_path(func):
    grid = [
    ['S', ' ', ' ', ' ', ' '],
    ['X', 'X', ' ', ' ', 'E'],
    [' ', ' ', 'X', ' ', ' '],
    ['X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ']
    ]
    start_point = (0, 0)
    end_point = (1, 4)
    expected_path = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4)]
    actual_path = func(grid, start_point, end_point)
    if expected_path == actual_path:
        print('Test Find Path Pass')
    else:
        print('Test Find Path Failed')
    return func


def test_get_neighbors(func):
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
        print('Test Get Neighbors Pass')
    else:
        print('Test Get Neighbors Failed')
    return func


def test_dfs(func):
    visited = [
    [False, False, False, False, False], 
    [False, False, False, False, False], 
    [False, False, False, False, False], 
    [False, False, False, False, False], 
    [False, False, False, False, False]
    ]
    maze = [
    ['S', ' ', 'X', 'X', 'E'],
    ['X', ' ', ' ', 'X', ' '],
    ['X', 'X', ' ', ' ', ' '],
    [' ', 'X', 'X', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ']
    ]
    expected_result = func(maze, 1, 1, visited, [])
    if expected_result:
        print('Test DFS Pass')
    else:
        print('Test DFS Failed')
    return func


def test_solve_maze(func):
    maze = [
    ['S', ' ', 'X', 'X', 'E'],
    ['X', ' ', ' ', 'X', ' '],
    ['X', 'X', ' ', ' ', ' '],
    [' ', 'X', 'X', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ']
    ]   
    expected_result = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (1, 4)]
    actual_result =  func(maze)
    if expected_result == actual_result:
        print('Test Solve Maze Pass')
    else:
        print('Test Solve Maze Failed')
    return func

