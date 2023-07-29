def test_schedule_task(func):
    tasks_list = [
    ('Task_A', 4.0, {'Resource_1': 2, 'Resource_2': 1}),
    ('Task_B', 7.0, {'Resource_2': 3}),
    ('Task_C', 5.2, {'Resource_1': 1})]
    resources_dict = {'Resource_1': 10, 'Resource_2': 15}
    deadline_time = 14.0
    expected_result = {'Resource_1': ['Task_A', 'Task_C', 'Task_B'], 'Task_A': 4.0, 'Task_C': 5.2, 'Task_B': 7.0}
    if (func(tasks_list, resources_dict, deadline_time)) == expected_result:
        print(f"Shedule Task Passed\n")
    else:
        print(f"Shedule Task  Failed\n")
    return func