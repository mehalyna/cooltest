def test_identify_risks(func):
    risks_list = [
        "Privacy concerns.",
        "Security vulnerabilities.",
        "Bias in AI algorithms."]
    expected_result = {"Privacy":"Privacy concerns.", "Security":"Security vulnerabilities.","Fairness":"Bias in AI algorithms."}
    actual_result = func(risks_list)
    print(actual_result)
    if actual_result == expected_result:
        print(f"Risk Task Passed\n")
    else:
        print(f"Risk Task  Failed\n")
    return func