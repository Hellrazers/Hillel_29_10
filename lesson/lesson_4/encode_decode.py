

str_to_encode = "hello world"
print(str_to_encode)
str_encode = str_to_encode.encode(encoding='windows-1251')
print(str_encode)

str_decode = str_encode.decode(encoding='windows-1251')
print(str_decode)

