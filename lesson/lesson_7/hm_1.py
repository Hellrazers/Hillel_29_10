lst_1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
count_r = 0
for i in lst_1:
    # if type(i) == int:
    if isinstance(i, int):
        count_r += int(i)
    elif isinstance(i, str) and i.isdigit():
        count_r += int(i)


def count_of_sum(list_obj: list) -> int:
    count_r = 0
    for i in list_obj:
        if type(i) == int:
        # if isinstance(i, int):
            count_r += int(i)
        elif isinstance(i, str) and i.isdigit():
            count_r += int(i)
    return count_r

print(count_r)

print(str.mro())
print(int(True))
print(int(False))
print(type(range(10)))
print(range.mro())
print(count_of_sum(lst_1))