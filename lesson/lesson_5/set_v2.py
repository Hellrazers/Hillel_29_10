set1 = {1, 2, 3}
set2 = {3, 4, 5}



set_union = set1.union(set2)
# set_union_2 = set1 | set2

print(set_union)
# print(set_union_2)

set_intersection = set1.intersection(set2)
print(set_intersection)

set_difference = set1.difference(set2)
set_difference_2 = set2.difference(set1)

print(set_difference)
print(set_difference_2)


set_symmetric_difference = set1.symmetric_difference(set2)
print(set_symmetric_difference)


#

set_comr = {k  if k % 2 == 0 else k - 1 for k in range(10)}
print(set_comr)


print({1, 0, 1, 0, True, False})

