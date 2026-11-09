str_1 = 'У цьому прикладі, якщо слово "пошук" знаходиться в рядку, програма виведе позицію першого входження. Якщо слово не знайдено, виведеться повідомлення про те, що підстрічка не знайдена.'

print(str_1.count('слово'))

word_to_find = 'слово'
index_word_start = str_1.find(word_to_find) # int
print(index_word_start)
print(str_1[index_word_start: len(word_to_find) + index_word_start])


print(str_1.find(word_to_find, index_word_start + len(word_to_find))) # len(word_to_find) -> int + int = result
print(str_1[106: len(word_to_find) + 106])

print(str_1.find('asdadasda'))
print(str_1.find('У'))
if str_1.find('asdadasda') == -1:
    print("нічого не знайшли")
