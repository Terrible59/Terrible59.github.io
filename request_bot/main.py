# -*- coding: utf8 -*-
import requests 
import json
from time import sleep

import myparser

# глобальные переменные 
TOKEN = '425662955:AAGK7JECeo-d9CiL8ryCkjS0HCZpSeh5BGA'
MAIN_URL = 'https://api.telegram.org/bot' + TOKEN + '/'
global last_upd
last_upd = 0

# функции
def req(method_name):
    """
        Функция в качестве аргумента принимает название метода, отправляет 
        http запрос на main url с данным методом и возвращает ответ 
        в виде json объекта. Функция json преобразует json объект
        в словарь для более удобной работы.
    """
    global TOKEN
    global MAIN_URL
    r = requests.get(MAIN_URL + method_name)
    return r.json()
def getMsg():
    """
         Функция не принимает никаких аргументов. Сначала отправляет http запрос
         с помощью выше описанной функции req, для получения обновлений. Далее 
         она получает id чата и текст сообщения и возвращает их в виде словаря.
    """
    upd = req('getUpdates')
    chat_id = upd['result'][-1]['message']['chat']['id']
    msg_text = upd['result'][-1]['message']['text']
    
    update_id = upd['result'][-1]['update_id']
    global last_upd
    if last_upd != update_id:
        message = {'chat_id': chat_id, 'text': msg_text, 'update_id': update_id}
        return message
    return None

def sendMsg(chat_id, text):
    """
        Функция принимает id чата и текст сообщения в качестве аргументов.
        Отправляет сообщение в чат, id которого указан в аргументе.
    """
    payload = {'chat_id': chat_id, 'text': text}
    return requests.get(MAIN_URL + 'sendMessage', params = payload)
def handleMsg(text):
    """
        Функция обрабатывающая текст сообщения.
    """
    ans = ''
    text = text.lower()
    if 'хорошо' in text:
        ans = myparser.getBtc()
    else:
        ans = 'Я таких комманд не знаю'
    return ans
# мои переменные


while True:
    msg = getMsg()
    if msg != None:
        uid = msg['update_id']
        last_upd = uid
        sendMsg(msg['chat_id'], handleMsg(msg['text']))
    else:
        continue
    #sleep(2)