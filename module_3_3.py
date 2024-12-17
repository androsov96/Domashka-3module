def print_params(a = 1, b = "Hello", c = True):
    print(a, b, c)
values_list = [3, "World", False]
values_dict = {"a": 5, "b": "Welcom", "c": 4.33}
values_list_2 = [54.32, "Привет Александр"]

#print_params(*values_list)
#print_params(**values_dict)
print_params(*values_list_2, 42)
