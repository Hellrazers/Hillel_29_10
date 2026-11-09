str_to_slice = 'Строки є незмінними, що означає, що після створення рядка ви не можете змінити його вміст без створення нового рядка (або перезапису вмісту змінної).'


print(str_to_slice[0])
print(str_to_slice[-1])


print(str_to_slice[5:30])
print(str_to_slice[29])



print(str_to_slice[::-1])

list_obj = list(range(1,10))
print(list_obj)


print(list_obj[::-1])


print(len(list_obj))
print(len(str_to_slice))
print(str_to_slice[148])



str_2 = 'Строки є незмінними'
list_of_str = list(str_2)
print(list_of_str)

for index, element in enumerate(list_of_str):
    if element == 'и':
        print(index)


str_3 = str_to_slice[-10:]
print(str_3)

str_4 = str_2 + ' ' + str_3
print(str_4)

print('-' * 150)

str_4 += str_4
print(str_4)