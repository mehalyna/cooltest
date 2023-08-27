def test_detect_color_task(func):
    image_path = 'sunflowers.png'
    expected_dominant_color = [ 7, 65, 46]
    expected_delta = 57.8
    act_dominant_color, act_percentage = func(image_path)
    if list(act_dominant_color) == expected_dominant_color and abs(expected_delta - act_percentage) <= 10:
        print(f"Schedule Task Passed\n")
    else:
        print(f"Schedule Task  Failed\n")
    return func