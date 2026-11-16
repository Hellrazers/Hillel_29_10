
# value = 'Hello World'
#
# for char in value:
#     print(char)


for i in range(1, 10):
    if i > 5:
        continue
    for j in range(5, 10):
        if j % 2 == 1:
            continue
        if j == 8:
            break
        print(f'{i} * {j} = {i * j}')

asd= r'''asasasasasasasasas'''

dot_number = None
for index,char in enumerate(asd):
    if char == '1':
        continue

    print(char)
else:
    print('LOG[DEBUG] : for in fuc os work correct')
        # dot_number = index


# print(dot_number)