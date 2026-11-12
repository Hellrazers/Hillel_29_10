MY_FEE = 20
MY_NAMES = ('oleksii', )

my_tuple = (1, 5, 3, 23)


my_tuple_1 = (1,)
print(my_tuple_1)
print(type(my_tuple_1))
print(my_tuple[:2])
print(my_tuple[2])
print(my_tuple.index(3))

my_tuple_3 = ('ivan', 'Olga',123, 23, 34, 'Olksii', 1)
*other_value, oleksii, int_value = my_tuple_3

print(other_value)
print(oleksii)
print(int_value)

ivan, *_, oleksii, _ = my_tuple_3
print(ivan)
print(oleksii)
print(my_tuple_3[0])
print(my_tuple_3[-2])


value_1, value_2 = 1, 2
print(value_1, value_2)
value_2, value_1 = value_1, value_2
# value_3 = None
# value_3 = value_1
# value_1 = value_2
# value_2 = value_3
print(value_1, value_2)



print(len(my_tuple_3))
# list_1  = list(range(1, 6))
#
# print(list_1)

# *_, third_elemnt, _, last_elemnt = list_1
# third_elemnt, last_elemnt = list_1[2], list_1[-1]
# print(last_elemnt)
# print(third_elemnt)