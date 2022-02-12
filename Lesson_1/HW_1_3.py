'''
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
'''

print('\nЗадание 3')
words = ['attribute', 'класс', 'функция', 'type']

flag = True
for word in words:
    try:
        word.encode('ascii')
    except:
        print(f'В байтовом типе (ascii) нельзя записать слово: {word}')
        flag = False

if flag:
    print('В байтовом типе (ascii) можно записать все заданные слова')


flag = True
for word in words:
    try:
        word.encode('utf-8')
    except:
        print(f'Нельзя записать в utf-8: {word}')
        flag = False

if flag:
    print('В utf-8 можно записать все из заданных слов')