# print(True == 1)
# print(False == 0)
# # print(True is 1)
# # print(False is 0)
#
# print(True is True)
# print(None is None)



age = 18

if age >= 18:
    print('Він дорослий')
elif age == 18:
    print('18')
elif 18 < age < 45:
    print('18 < 45')
else:
    print('все інше ')

# if 18:
# elif 45:
# elif 18+:
# else:


if age == 18:
    print('йому 18')

result = 'дорослий' if age >= 18 else 'Ne дорослий'

print(result)

list_values = ('asdasd',)
print(isinstance(list_values, str))
print(type(list_values) == list)
if list_values and (isinstance(list_values, str) or type(list_values) == list): # if True
    print('asdasdasdasd')
elif list_values and isinstance(list_values, tuple):
    list_1 = []
    for item in list_values:
        list_1.append(item)



# def list_value(list_value = None):
#     list_values = [] or list_value
#     print(list_values)
#     list_values = []
#     if not list_value:
#         list_value = []
# if list_values and (isinstance(list_values, tuple) or type(list_values) == list):

# bool_1 = True
# print(isinstance(bool_1, int))
# print(bool.mro())

v_ = {'audi': ('silver', 2019, 1.8, 'sedan', 50000)}
# if v_[1] == 2019 and v_[2] >=1.8:
#     pass
if v_.get('audi'):
    print(v_.get('audi')[1] == 5)