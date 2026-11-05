from numpy.ma.extras import average

value_str = 'Літерал — це пряме позначення в програмі значення даних (числа, рядка або контейнера). Нижче наведено числові та рядкові літерали в Python.'

print(value_str[19:35:-1]) #[ВІД_ЯКОГО_ЕЛЕМНТУ_ВКЛЮЧНО:ДО_ЯКОГО_ЕЛЕМНТУ_НЕВКЛЮЧНО:КРОК]
print(len(value_str))
print(value_str[::-1])

list_1 = [1,2 ,3, 4, 5]
print(list_1[::-2])
print(value_str[138])
print(value_str[-5])

list_2 = list_1
print(list_2[:3])
set_value = {1, 2,2, 1,2}
dict_value = {'id':1, 'value': 5}
for item in dict_value: # {1, 2}
    print(item)





list_1 = [3 ,3, 4, 5, 10, len('1231')]

print(min(list_1))
print(max(list_1))
print(sum(list_1))
print(average(list_1))

