def test_search_word(func):
    word = "APPLE"
    grid = [['A', 'P', 'P', 'L'], ['E', 'F', 'G', 'E'], ['I', 'J', 'K', 'G'], ['M', 'N', 'H', 'P']]
    
    if func(grid, word):
        print('Test Display Word pass')
    else:
        print('Test Display Word failed')
    return func
