

str_1 = 'Функція split() використовується для розділення рядка на частини на основі певного роздільника та повертає список отриманих частин. Основні варіанти використання split():'

# print(*str_1.split(), sep='\n')
#
#
# print(str_1.split(sep='split()'))


# if 'рядка' in str_1:
#     print(True)

list_of_words = str_1.split()
print(len(list_of_words))
print(list_of_words)
for index, word in enumerate(list_of_words):
    if word.startswith('в'):
        print(index)
    if word.startswith('split'): #-> word == split()
        list_of_words[index] = 'split'
print(list_of_words)


list_of_words = str_1.split(maxsplit=1)
print(list_of_words)
print(len(list_of_words))




import re
рядок = "apple1 orange1,banana1"
частини = re.split(r'\d+', рядок)
print(частини)
# Результат: ['apple', 'orange,banana']
