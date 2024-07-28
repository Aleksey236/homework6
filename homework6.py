my_dict = {'Alex': 2003, 'Sasha': 2001}
print(my_dict)
print('Existing value:', my_dict['Alex'])
print(my_dict.get('Anton'), 'Not existing value: None')
my_dict['Roma'] = 1955
my_dict['Dima'] = 1999
a = my_dict.pop('Dima')
print('Deleted value:', a)
print(my_dict)

my_set = {True, 1, 1, 2, 3, 2, True, False, (1, 2, 3)}
print(my_set)
print(my_set.add(4))
print(my_set.add(5))
print(my_set.remove((1, 2, 3,)))
print(my_set)