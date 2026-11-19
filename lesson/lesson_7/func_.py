import random

def first_func(some_value, other_value):
    print('Hello world')
    some_value += other_value
    return some_value, other_value


asd = first_func(1, 2)
second_fn = first_func(some_value=1, other_value=2)
third_fn = first_func(other_value=1, some_value=2)

print(type(asd))


def sc_fn(first: int | float, second: str) -> str:
    '''
    ми вводимо 2 параметри і множимо стр на інт
    :param first: якись стр паметр...
    :param second: якись int паметр...
    :return: result of pow this action
    '''
    value_ = f'{first} world' * second
    return value_


print(sc_fn(second=4, first='Hey'))

first_v = []


def fn_3():
    value_to_add = random.choice(list('stasdasdasdasd'))
    first_v.append(value_to_add)
    return first_v


fn_3()
fn_3()
print(first_v)


sec_v = 5
def fn_4(sec_v):
    # global sec_v
    value_to_add = random.choice(range(1, 100))
    # print(value_to_add)
    sec_v += sec_v
    return sec_v

#fn -> 5 + 5 = 10
#fn -> 10 + 10 -> 20
first_1 = fn_4(5)
senond_2 = fn_4(first_1)
print(senond_2)


print(fn_4(fn_4(5)))
# print(sec_v)