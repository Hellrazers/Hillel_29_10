# list_l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, '123']
#
# print(list(map(lambda x: x * 5, list_l)))
# print([k * 5  for k in list_l if type(k) == int and k >= 5])
#
#
# list_of_words = ['apple', 'banana', 'cherry']
# upper_words = list(map(str.upper, list_of_words))
# print(upper_words) # ['APPLE', 'BANANA', 'CHERRY']
# print([k.upper() for k in list_of_words])
#
#
# import datetime
# print(datetime.datetime.now())
# list_l = range(100000000)
# v = (map(lambda x: x * 2, list_l))
# # v = [ k * 2  for k in list_l]
# print(datetime.datetime.now())
# print(next(v))
# print(list(v)[-1])



list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped =list(zip(list1, list2))
print((zipped))
print(dict((zipped)))
print({ v:list2[index] for index, v in enumerate(list1) })

print(all([True, '', 1]))

list_r = range(1, 5)
list_b = [k % 2 == 0 for k in list_r]
print(list_b)
print(all(list_b))
print(any(list_b))
print(all(k % 2 == 0 for k in list_r))


frozenset = frozenset(list_r)
print(frozenset)
frozenset.add(1)
print(frozenset)