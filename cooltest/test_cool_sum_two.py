def test_sum_two(func):
    a, b = 2, 3
    expected_result = 5
    actual_result = func(a, b)
    if expected_result == actual_result:
        print('Test Sum pass')
    else:
        print('Test Sum failed')
    return func