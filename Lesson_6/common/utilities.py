"""Утилиты"""
import sys,os
sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append('../')
import json

from errors import IncorrectDataRecievedError, NonDictInputError

from common.variables import MAX_MESSAGE_SIZE, ENCODING
from decos import log


@log
def get_message(client):
    '''
    Утилита приёма и декодирования сообщения
    принимает байты выдаёт словарь, если принято что-то другое, выдает ошибку значения
    '''

    encoded_response = client.recv(MAX_MESSAGE_SIZE)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError

@log
def send_message(sock, message):
    '''
    Утилита кодирования и отправки сообщения
    принимает словарь и отправляет его на сервер
    '''
    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)