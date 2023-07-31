def test_identify_risks(func):
    risks_categories = [['Privacy', 'Privacy concerns: AI-powered devices may collect personal data, raising concerns about how this data is stored and used.'], 
                        ['Security', 'Security vulnerabilities: AI systems could be susceptible to cyberattacks, leading to unauthorized access to personal information.'], 
                        ['Fairness', 'Bias in AI algorithms: AI algorithms might inadvertently perpetuate biases present in the data they are trained on, leading to unfair or discriminatory outcomes.']]
    expected_result = {'privacy': ['Privacy concerns: AI-powered devices may collect personal data, raising concerns about how this data is stored and used.'], 
                       'security': ['Security vulnerabilities: AI systems could be susceptible to cyberattacks, leading to unauthorized access to personal information.'], 
                       'fairness': ['Bias in AI algorithms: AI algorithms might inadvertently perpetuate biases present in the data they are trained on, leading to unfair or discriminatory outcomes.']}
    actual_result = func(risks_categories)
    print(actual_result)
    if actual_result == expected_result:
        print(f"Risk Task Passed\n")
    else:
        print(f"Risk Task  Failed\n")
    return func