"""Программа-сервер"""
import argparse
import socket
import sys, os
import json
import logging
import log.server_log_settings
from errors import IncorrectDataRecievedError
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from common.utilities import get_message, send_message
from socket import socket, AF_INET, SOCK_STREAM
from decos import Log, log
from log.server_log_settings import LOGGER as SERVER_LOGGER  # Инициализация логирования сервера.


@log
def process_client_message(message):
    """
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента
    :param message:
    :return:
    """
    SERVER_LOGGER.debug(f'Разбор сообщения от клиента : {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

@log
def create_arg_parser():
    """Парсер аргументов коммандной строки"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    return parser

def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    Сначала обрабатываем порт прописывая в командной строке или запуская через PyCharm:
    server_side.py -p 7777 -a 127.0.0.1
    Или при использовании Windows 10:
    .\server_side.py -p 7777 -a 127.0.0.1
    """

    try:
        if '-p' in sys.argv:
            serv_listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            serv_listen_port = DEFAULT_PORT
        if serv_listen_port < 1024 or serv_listen_port > 65535:
            SERVER_LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта '
                                   f'{serv_listen_port}. Допустимы адреса с 1024 до 65535.')
            raise ValueError
        SERVER_LOGGER.info(f'Запущен сервер, порт для подключений: {serv_listen_port}, ')
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            serv_listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            serv_listen_address = ''
        SERVER_LOGGER.info(f'Адрес с которого принимаются подключения: {serv_listen_address}. '
                           f'Если адрес не указан, принимаются соединения с любых адресов.')

    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Готовим сокет

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((serv_listen_address, serv_listen_port))

    # Слушаем порт

    server_socket.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = server_socket.accept()
        SERVER_LOGGER.info(f'Установлено соедение с ПК {client_address}')
        try:
            message_from_client = get_message(client)
            SERVER_LOGGER.debug(f'Получено сообщение {message_from_client}')
            response = process_client_message(message_from_client)
            SERVER_LOGGER.info(f'Сформирован ответ клиенту {response}')
            send_message(client, response)
            SERVER_LOGGER.debug(f'Соединение с клиентом {client_address} закрывается.')
            client.close()
        except json.JSONDecodeError:
            SERVER_LOGGER.error(f'Не удалось декодировать JSON строку, полученную от '
                                f'клиента {client_address}. Соединение закрывается.')
            client.close()
        except IncorrectDataRecievedError:
            SERVER_LOGGER.error(f'От клиента {client_address} приняты некорректные данные. '
                                f'Соединение закрывается.')
            client.close()


if __name__ == '__main__':
    main()