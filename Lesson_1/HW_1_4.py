'''
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
 и выполнить обратное преобразование (используя методы encode и decode).
'''

print('\nЗадание 4')
words = ['разаботка', 'адмиинстрирование', 'protocol', 'standard']

for word in words:
    res_enc = word.encode(encoding='utf-8')
    res_dec = res_enc.decode(encoding='utf-8')
    print(f'{res_enc} - {res_dec}\n')