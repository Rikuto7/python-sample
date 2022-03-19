numbers = [1, 2, 3]
a, b, c = numbers


def print_numbers(first, second, third):
    print("1番目: ", first)
    print("2番目: ", second)
    print("3番目: ", third)

print_numbers(*numbers)


def print_dict(data3, data2, data1):
    print("data1: ", data1)
    print("data2: ", data2)
    print("data3: ", data3)

dict_data = {
    "data1": 1,
    "data2": 2,
    "data3": 3
}

print_dict(**dict_data)
