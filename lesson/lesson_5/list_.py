
list_1 = [1, 2, 3]
list_2 = []
list_3 = [1]
print(list_1)
print(list_2)
print(list_3)
print(list_1[0])
list_1[0] = 2
print(list_1[0])

#adding
(list_1.append('123123'))
print(list_1)
list_1.insert(0, 555)
print(list_1)

#remove element
list_1.remove(3)
print(list_1)
list_1.pop()
print(list_1)
list_1.pop(0)
print(list_1)

list_4 = list(range(5, 10))
print(list_4)
# list_1.extend(list_4)
# print(list_1)

list_5 = [*list_1, *list_4]
print(list_5)
print(len(list_5))


#copy
list_copy = [1, 2, 3]
# list_to_copy = list_copy[:]
list_to_copy = list_copy.copy()

list_copy.append(234)
print(id(list_copy))
print(list_copy)
print(id(list_to_copy))
print(list_to_copy)

from copy import deepcopy
#deepcopy
list_to_copy_1 = [1, 2, 3, [1, 2, 3]]
list_to_copy_2 = deepcopy(list_to_copy_1)
list_to_copy_1.insert(1, 'asdasd')
list_to_copy_1[-1].append('asdasdasd')
print(list_to_copy_1)
print(list_to_copy_2)
print(id(list_to_copy_1[-1]))
print(id(list_to_copy_2[-1]))
