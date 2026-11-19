

def sc_fn(first= 2, second = 1):
    return first + second

# print(sc_fn(1, 2))
# print(sc_fn(1))
# print(sc_fn())


def sc_list_2 (first, list_ = None):
    list_ = list_ or []
    list_.append(first)
    return list_

print(sc_list_2(1))
print(sc_list_2(2))


