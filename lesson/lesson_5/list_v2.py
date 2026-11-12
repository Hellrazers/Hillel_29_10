list_1 = list(range(10))
print(list_1)
# list_2:list = []
# for value in list_1:
#     if value % 2 == 0:
#         list_2.append(value)
list_4 = [value for value in list_1 if value % 2 == 0] # [value(значення яке ми будемо записувати) for(далі типовий цикл) value in iter_obj if умова_якась]

list_2:list = []
for value in list_1:
    if value % 2 == 0:
        list_2.append(value)
    else:
        list_2.append(value * 10)

list_3 = [value if value % 2 == 0 else value * 10 for value in list_1 ] # [value(значення яке ми будемо записувати) if умова_якась for(далі типовий цикл) value in iter_obj ]

print('list:3 ',list_3)
# print(list_2)

def some_func(x):
    for value in x:
        len(value)

#sort
list_3.sort()
print(list_3)

list_4 = ['xasasd', 'asdasd', 'asd', 'cs','z', 'rasdssss', 'asssssssss']
list_5 = sorted(list_4, reverse=True, key=lambda value: len(value))

# list_4.sort(key=lambda x: len(x))
list_4.sort(reverse=True, key=lambda value: len(value) )
# list_4.sort(True, lambda x: len(x) )
print(list_5)
print(list_4)
print(list_3)

#filter
list_5 = list(filter(lambda v: v > 10, list_3))
print((list_5))
list_6 = [value for value in list_3 if value > 10]
print(list_6)

#map
list_7 = list(map(lambda v: pow(v, 2) , list_5))
list_7 = list(map(lambda v: len(str(v)) , list_7))

print(list_7)
print([pow(v, 2) for v in list_5 ])
