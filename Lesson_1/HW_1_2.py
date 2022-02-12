'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов 
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''

print('\nЗадание 2')
words = [b'class', b'function', b'method']

for word in words:
    print(f'тип: {type(word)}, содержимое: {word}, длина: {len(word)} символов')