# list
int_list = [x for x in range(10) if x % 2 == 1]
int_list2 = [x if x % 2 == 1 else None for x in range(10)]
int_list.append(100)
int_list.remove(100)
int_list.pop()

int_list.reverse()
reverse_list = reversed(int_list)
int_list.sort(reverse=False, key=abs)
sort_list = sorted(int_list)

list1 = [1, 2, 3]
list2 = [3, 4, 5]
list3 = [*list1, *list2]
list3 = list1 + list2


# dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {**dict1, **dict2}
dict1.update(dict2)
value = dict1.setdefault('a', 5)  # 1
value = dict1.setdefault('e', 5)  # 5
del dict1['a']
dict1.pop('a', None)
dict1['new_a'] = dict1.pop('a')


# set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 - set2
set4 = set1 & set2
set5 = set1 | set2
set6 = set1 ^ set2
set1.add(100)
set1.remove(100)

# 三項演算子
x = 10
s = 'positive' if x > 0 else 'negative'
s = 'positive' if x > 0 else 'negative' if x < 0 else 'zero'


# lambda
list1 = ['1', '2', '3', '4', '5']
result = list(map(lambda x: int(x), list1))


# class
class Person(object):

    kind = "human"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def introduce(self):
        print(self.name)
        self.say_something('something')

    def say_something(self, something):
        print(something)

    @classmethod
    def what_kind(cls):
        print(cls.kind)

    @staticmethod
    def base_func():
        print("ok")

    def __del__(self):
        print('done')
