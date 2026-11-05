try:
    input_value = int(input("Скільки тобі років: "))
except ValueError as e:
    print(e)
print(input_value)
print(type(input_value))
try:
    if 18 <= input_value < 60:
        print('Ти можеш куприти алкоголь')
    elif input_value < 18:
        print('Забoрона')
    elif input_value >= 60:
        print('Не раджу вживати алкоголь')
except ValueError as e:
    print(e)
