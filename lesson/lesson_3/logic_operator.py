
value = 1234
print(int(value*(-1)))
print(abs(value))

if value < 0:
    print(f'{abs(value)} нижче нуля')
elif value > 0:
    print(f'{value} вище нуля')
else:
    print("0 Градусів")

my_tuple = (1, )


value_str = 'Літерал — це пряме позначення в програмі значення даних (числа, рядка або контейнера). Нижче наведено числові та рядкові літерали в Python.'

print(value_str[19:35:-1]) #[ВІД_ЯКОГО_ЕЛЕМНТУ_ВКЛЮЧНО:ДО_ЯКОГО_ЕЛЕМНТУ_НЕВКЛЮЧНО:КРОК]
print(len(value_str))
print(value_str[::-1])

list_1 = [1,2 ,3, 4, 5]
print(list_1[::-2])
print(value_str[138])
print(value_str[-5])

{'id':1}
{1,2,3,4,5,'asd', 423, 234}


value_1, value_2, value_3, value_4, value_5, value_6, value_7 = 1, 2, 3, 4, 5, 6, 7

value_1, value_2 = 123, 34534
value_1 = 23; value_2 = 333
print(value_1, value_2)
class A:
    pass

print(len(value_str))
print(value_str.__len__())
