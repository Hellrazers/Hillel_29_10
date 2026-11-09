# str_1 = 'Методи .startswith() та .endswith() використовуються для перевірки того, чи рядок починається або закінчується певною підстрічкою.'
#
#
#
# print(str_1.startswith('М'))
# print(str_1.startswith('Методи '))
# print(str_1.startswith('    М'))
#
# print(str_1.endswith('.'))
# print(str_1.endswith('підстрічкою.'))
# print(str_1.endswith('    . '))
#
#
# str_2 = '             Методи .startswith() та .ends або закінчується певною підстрічкою.          '
# str_3 = '!!!!!!!!!!Методи .startswith() та .ends або закінчується певною підстрічкою.!!!!!!!!!!!!!'
#
# print(str_2.lstrip())
# print(str_2.rstrip())
# print(str_2.strip())
#
#
# print(str_3.lstrip('!'))
# print(str_3.rstrip('!'))
# print(str_3.strip('!'))
#
#
# print(str_3.lstrip('!').upper().split())



str_4 = '23.12'
print(float(str_4))
if str_4.isdecimal():
    print(int(str_4))


str_5 = "1,2,3,4,5"
tuple_1 = tuple(str_5.split(","))
print(tuple_1)
print(tuple_1[0] + tuple_1[1])


digigt_ = 3.14159265359
row = f"Значення числа: {digigt_:.5f}"  # Виводить 2 знаки після коми
print(row)

str_6 = 'Методи'
print(str_6.startswith('Ме') and str_6.endswith('ди'))



str_7 = '''Функція split() використовується для розділення рядка на частини на основі певного роздільника та повертає список отриманих частин. Основні варіанти використання split():

Розділення за пробілом:

Якщо не вказати конкретний роздільник, split() використовує пробіли (і інші пробільні символи) як роздільники.'''

print(len(str_7.split('\n')))
list_1 = str_7.split('\n')
print(list_1)
# list_2 = [] # list_2 [value for value in list_1 if value ]
# for value in list_1:
#     if value:
#         list_2.append(value)
list_2 = [value for value in list_1 if value]
print(len(list_2))
print(list_2)

list_3 = []
for value in list_2:
    list_3.extend(value.split('. '))

print(list_3)