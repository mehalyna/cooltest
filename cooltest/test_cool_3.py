def test_schedule_task(func):
    tasks_list = [
    ('Task_A', 4.0, {'Resource_1': 2, 'Resource_2': 1}),
    ('Task_B', 7.0, {'Resource_2': 3}),
    ('Task_C', 5.2, {'Resource_1': 1})]
    resources_dict = {'Resource_1': 10, 'Resource_2': 15}
    deadline_time = 14.0
    expected_result = {'Resource_1': ['Task_A', 'Task_C', 'Task_B'], 'Task_A': 4.0, 'Task_C': 5.2, 'Task_B': 7.0}
    if (func(tasks_list, resources_dict, deadline_time)) == expected_result:
        print(f"Schedule Task Passed\n")
    else:
        print(f"Schedule Task  Failed\n")
    return func


def test_optimize_vrp(func):
    depot_location = (0, 0)
    customer_locations = [(1, 3), (3, 5), (4, 8), (9, 6), (7, 1)]
    capacity_per_vehicle = 3
    number_of_vehicles = 2
    expected_result = [[(9, 6), (4, 8), (3, 5), (1, 3)], [(7, 1)]]
    if (func(depot_location, customer_locations, capacity_per_vehicle, number_of_vehicles)) == expected_result:
        print(f"VRP Task Passed\n")
    else:
        print(f"VRP Task  Failed\n")
    return func


