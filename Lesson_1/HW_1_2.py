'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов 
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''
STR_A = 'class'
STR_B = 'function'
STR_C = 'method'

STR_LIST = [STR_A, STR_B, STR_C]

for el_str in STR_LIST:
    el = eval(f"b'{el_str}'")
    print('=' * 50)
    print('type: ', type(el))
    print(el)
    print('length of variable in bytes: ', len(el))