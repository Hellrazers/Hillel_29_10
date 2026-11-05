# #немутабельна об'єкти
#
# # value_int = 2344
# #
# # print(id(value_int)) #2059882903248
# #
# # value_int += 1
# # print(id(value_int))
# #
# # print(80 * '-')
# # str_value = 'Привіт'
# # print(id(str_value))
# # str_value += ' ворд'
# # print(id(str_value))
# #
# # print(80 * '-')
# #
# # tuple_value = (1, 2, 3)
# # print(id(tuple_value))
#
# print(80 * '-')
#
# list_1 = [1, 2, 3]
# print(id(list_1))
# list_1.append(4)
# print(id(list_1))
#
#
# list_2 = list_1
#
# print(f'list_2 = {list_2}')
#
# list_1.append(5)
# print(f'list_2 = {list_2}')
# print(f'list_1 = {list_1}')
#
# print(f'id(list_2) = {id(list_2)}')
# print(f'id(list_1) = {id(list_1)}')
#
# list_3 = list_1[:]
# print(f'id(list_3) = {id(list_3)}')
#
# list_1 = [1, 2, 3]
#
#


def my_function( value, list_1 = []):
    list_1.append(value) # [].append(1) -> 53-> [1].append(5)
    print(list_1)

my_function(1)
my_function(5)



