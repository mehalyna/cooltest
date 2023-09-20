def test_search_word(func):
    word = "ROCK"
    grid = [['A', 'B', 'C', 'R'], ['E', 'F', 'G', 'O'], ['I', 'J', 'K', 'C'], ['M', 'N', 'O', 'K']]
    
    if func(grid, word):
        print('Test Display Word pass')
    else:
        print('Test Display Word failed')
    return func
