'''
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
'''

import json


def write_order_to_json(item, quantity, price, buyer, date):
    """Функция записи в json"""

    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8', ) as f_in:
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)

        json.dump(data, f_in, indent=4, ensure_ascii=False)


# initialisation (чтобы не удалять данные при каждой новой проверке скрипта)
with open('orders.json', 'w', encoding='utf-8') as f_in:
    json.dump({'orders': []}, f_in, indent=4)


write_order_to_json('Видеокарта Palit GeForce RTX 3050 StormX', '2', '62900', 'Lymzin A.G.', '09.02.2022')
write_order_to_json('Процессор Intel Core i5-10400F OEM', '5', '11899', 'Kudrin F.Q.', '19.01.2022')
write_order_to_json('Монитор LG UltraGear 27GL83A-B черный', '7', '27899', 'Кукушкин В.А.', '30.12.2021')