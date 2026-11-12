my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, (1,): 5, True:6, 1+1: 7, "123123":1123123}
print(my_dict)
asd = 'aaa'
asdf = 'aaa'
print(id(asd))
print(hash(asd))
print(id(asdf))
print(hash(asdf))
print(hash(asd) == hash(asdf))
print(hash(True))

# print(hash((1,2, [1])))

#GET
# print(my_dict['123'])

print(my_dict.get('123123', 'НІЧОГО НЕ ЗНАЙШЛО'))
if my_dict.get('123123') :
    print(my_dict.get('123123'))


#add
my_dict['222'] = 123
print(my_dict)




my_dict_2 ={'a': 6, 'b': 5, 'f': 4}


# my_dict.setdefault(*my_dict_2.keys())
print(my_dict)
# my_dict.update(my_dict_2)
# print(my_dict)



#delete
print(my_dict.pop('c'))
print(my_dict)


#dict_compr

# dict_comp = {k:v * 10 for k, v in my_dict.items() if v > 0}
#
# for k,v in my_dict.items():
#     if k == 'a':
#         print(v)
#     elif k == 'b':
#         print(v)

# tuple_1 = ('a', 'b', 'c', [1, 2])
# tuple_1[-1].append('asdasdad')
#
# tuple_1[1] = 'asdasdad'
# print(tuple_1)
# print(list(tuple_1))


list_1 = ['first', 'second', 'third',4]
list_2 = [1,2, 3]

list_4 = list(zip(list_1, list_2))
print(list_4)
print(dict(list_4))

dict_3 = {'id': 123,
          'name': 'asd',
          'tags': [1, 2, 3, 4],
          'meta_data': [
              {'id': 1,
               'value': 2}
          ]}

print(dict_3)
print(dict_3.get('meta_data')[0]['value'])