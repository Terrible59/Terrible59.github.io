# -*- coding: utf8 -*-
import requests 
import json
from time import sleep

import myparser

# ���������� ���������� 
TOKEN = '425662955:AAGK7JECeo-d9CiL8ryCkjS0HCZpSeh5BGA'
MAIN_URL = 'https://api.telegram.org/bot' + TOKEN + '/'
global last_upd
last_upd = 0

# �������
def req(method_name):
    """
        ������� � �������� ��������� ��������� �������� ������, ���������� 
        http ������ �� main url � ������ ������� � ���������� ����� 
        � ���� json �������. ������� json ����������� json ������
        � ������� ��� ����� ������� ������.
    """
    global TOKEN
    global MAIN_URL
    r = requests.get(MAIN_URL + method_name)
    return r.json()
def getMsg():
    """
         ������� �� ��������� ������� ����������. ������� ���������� http ������
         � ������� ���� ��������� ������� req, ��� ��������� ����������. ����� 
         ��� �������� id ���� � ����� ��������� � ���������� �� � ���� �������.
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
        ������� ��������� id ���� � ����� ��������� � �������� ����������.
        ���������� ��������� � ���, id �������� ������ � ���������.
    """
    payload = {'chat_id': chat_id, 'text': text}
    return requests.get(MAIN_URL + 'sendMessage', params = payload)
def handleMsg(text):
    """
        ������� �������������� ����� ���������.
    """
    ans = ''
    text = text.lower()
    if '������' in text:
        ans = myparser.getBtc()
    else:
        ans = '� ����� ������� �� ����'
    return ans
# ��� ����������


while True:
    msg = getMsg()
    if msg != None:
        uid = msg['update_id']
        last_upd = uid
        sendMsg(msg['chat_id'], handleMsg(msg['text']))
    else:
        continue
    #sleep(2)