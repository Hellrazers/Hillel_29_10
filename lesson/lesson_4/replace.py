str_1 = 'Метод .replace() використовується для заміни входжень певної підстрічки іншою підстрічкою в рядку. Ось приклад використання:'

print(str_1.replace('о', '1111111').replace('О', '22222222'))

list_1 = str_1.split()
list_2 = []
for letter in list_1:
    list_2.append(letter.lower().replace('о', '222').title())

print(list_2)

print(' '.join(list_2))