def test():
    test_list = ["kula", "kula", "kula", "kula", "kula"]
    test_num_list = []
    for x in range(1,11):
        test_num_list.append(x)
    test_num_list.sort(key=None,reverse=True)
    if all(x == "kula" for x in test_list):
        print(sum(test_num_list, test_num_list[9]))

    test_num_list = sorted(test_num_list)
    print(test_num_list)

    string_s = "string"
    print(string_s[1])
    string_s =''.join(test_list)
    print(string_s)