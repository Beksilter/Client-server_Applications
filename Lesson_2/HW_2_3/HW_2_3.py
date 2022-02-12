"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

input_data = {'items': ['motherboard', 'graphics card', 'CPU', 'RAM','SSD'],
           'items_quantity': 14,
           'items_price': {'Motherboard': '80€-200€',
                           'Graphics card': '650€-800€',
                           'CPU': '500€-600€',
                           'RAM': '100€-150€',
                           'SSD': '120€-180€' }
           }

with open('file_1.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(input_data, f_in, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open("file_1.yaml", 'r', encoding='utf-8') as f_out:
    output_data = yaml.load(f_out, Loader=yaml.SafeLoader)

print(input_data == output_data)
