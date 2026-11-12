# set_1 = {1, 1, 1,2}
# print(set_1)

list_1 = [1345, 1345, 1345,2345, True]
# print(set(list_1))
set_1 = set()
list_2 = []
for item in list_1:
    if not item in set_1:
        list_2.append(item)
        set_1.add(item)

print(set_1)
print(list_2)


print(hash(1))
print(hash(True))

set_1.add(3)
print(set_1)
# print(set_1.pop())

set_1.remove(1345)
print(set_1)


my_set = {15345, 2345123, 3234}
additional_elements = {432, 5534, 6234}

my_set.update(additional_elements)
print(my_set)


print(all(['', True, True, True]))
print(any([True, False]))