def no_lambda(x):
    return x ** 2


value_1 = lambda x: x ** 2


print(no_lambda(2))


def no_lambda_2 (x):
    return x >= 5

list_l = list(range(10))
print(list_l)
print(list(filter(lambda x: x >= 5, list_l)))
print(list(filter(no_lambda_2, list_l)))
