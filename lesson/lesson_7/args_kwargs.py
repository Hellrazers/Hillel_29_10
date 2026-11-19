
first_l = [1,2, 3]
second_2 = 'asdas'
third_3 =  True
lst_v = (1,)
def say_something(first, second, third):
    if type(first) == list:
        print('LLIIIST')
    if type(second) == str:
        print('SSSSSSTTTTTTTTRRRRRRR')
    if type(third) == bool:
        print('BOOOOOLLLLLLL')


say_something(first_l, second_2, third_3)

def say_something_v2(*args):
    print(args)
    print(len(args))
    for element_in_args in args:
        # print(type(element_in_args))
        if type(element_in_args) == list:
            print('LLIIIST')
        elif type(element_in_args) == str:
            print('SSSSSSTTTTTTTTRRRRRRR')
        elif type(element_in_args) == bool:
            print('BOOOOOLLLLLLL')

say_something_v2(first_l, second_2, third_3, lst_v, *list(range(100)))
say_something_v2(*first_l, *second_2, third_3, lst_v)
say_something_v2()


def say_something_vkwargs(**kwargs):
    print(kwargs)
    for element_in_args, value in kwargs.items():
        # print(type(element_in_args))
        if type(element_in_args) == list:
            print('LLIIIST')
        # elif type(element_in_args) == str:
        #     print('SSSSSSTTTTTTTTRRRRRRR')
        elif type(element_in_args) == bool:
            print('BOOOOOLLLLLLL')
        elif element_in_args == 'id':
            print(f'value = {value}')
dict_value = {'id':1, 'asd': True, 'value': [123,1,1,1]}


say_something_vkwargs(**dict_value) # **dict_value == (id=1, asd=True, value=[123,1,1,1])
say_something_vkwargs(asdasd=123, sec=33, third = True, other=123 )



def last_r (*args, **kwargs):
    print(args)
    print(kwargs)

last_r(1, 2, 3, id=5, k= 6)


# def request(method, url,headers, params=None, json=None, ):
#     print(f'request.with.METHOD:{method}.url:{url}')

def request(method, url, **kwargs):
    if method == 'GET':
        print(f'{method} {url} with {kwargs.get('params')}')
    elif method == 'POST':
        print(f'{method} {url} with {kwargs.get("json")}')
request('GET', 'http://www.google.com')
request(method='GET', url='http://www.google.com', params={'param1': 'value1', 'param2': 'value2'})
request(method='POST', url='http://www.google.com', params={'param1': 'value1', 'param2': 'value2'}, json={'js1': 'value1', 'js2': 'value2'})




