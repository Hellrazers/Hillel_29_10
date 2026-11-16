
# int_v = 0
# while int_v < 10:
#     print(int_v)
    # int_v += 1


# some_value = int(input('Enter some value: '))
#
# while some_value == 100:
#     print('some_value')
#     some_value = int(input('Enter some value: '))


# :=
# while (some_value := int(input('Enter some value: '))) != 100:
#     print(some_value)
#     if some_value == 1:
#         break


# while (value := first_v)  != compare_v


import time

start_time = time.time()

while (time_now := time.time()) - start_time < 10:
    print(time_now - start_time)
    time.sleep(1)


# list_1 = list(range(10000000))