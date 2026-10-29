hello_word = "Hello World"
# print(hello_word)
#
# type_of_hello_word = type(hello_word)
# print(type_of_hello_word)
# print(type(hello_word))



#string
type_value: str = '123'
print(type(type_value))


print(type_value[:2])
# print([1, 2,4 ,3 ,45])


#values
int_value: int = 1
float_value: float = 3.14
div_res = 4 / 2
print(type(div_res))
print(int)

print(5/3)
print(int(5/2))
print(round(5 / 3, 5))

value_str =str(1.6666666666666667)
print(value_str[:4])


div_res = 4 / 2
print(f' our div res === {div_res}')

def div_2_veriables(a: int | float, b: int | float):
    print(round(a / b, 3))

div_2_veriables(234, 23)


#boolean
#TRUE FALSE

if type(div_res) is float:
    print('This is a float')
else:
    print("This is other value")


print(type(div_res) is float)
#None
value_str = '' # пустата буде None
# print(value_str is not None)
print(value_str is None)
if value_str:
    print(value_str)
else:
    print('This is empty string')


vy_tuple  = (1, 2 ,3)
my_set = {1, 2234, 435 ,5, 'asdas', 5}
my_list = list(vy_tuple)
my_dict = {
    'name': 'John',
    'age': 21,
}

print(my_set)

my_tuple = (1, 2234, 435 ,5, 'asdas', 5)

my_set_2 = set(my_tuple)
print(type(my_set_2))
print(my_set_2)
print(len(my_tuple))
print(len(my_set_2))
print(len(my_tuple) == len(my_set_2))
# 12asd

def div_2_veriables(a: int | float, b: int | float):
    print(round(a / b, 3))

    return {1, 2, 3}, [1, 2, 3]

print((div_2_veriables(1, 2)))

print(type(div_2_veriables(1, 2)))

list_2 = [1, {1,2}, {1:4}, {True:123}]
print(list_2)

list_2.append(5)
list_2.remove(1)

list_2.pop(0)
print(list_2)

set_2 = {1, 2, 3}
print(set_2)
apple_value = 5
peanapple_value = 5
tomato= 5
print('Всього у нас було apple:', apple_value, ', peanapple:', peanapple_value , ', tomato:', tomato, 'а загалом у нас:', apple_value + peanapple_value+tomato)


print(f'Всього у нас було apple: {apple_value + 100}, peanapple: {peanapple_value}, len {len('tomato')}:{tomato} загалом у нас: {apple_value + peanapple_value + tomato}')

if apple_value == 5:
    print(apple_value)


hello_word = "Hello World"
print('Helllo word len: ',len(hello_word))
for values in my_tuple:
    print(values)


# str
# bool
# int

