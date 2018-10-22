import telebot
import constants
import text
import os
bot = telebot.TeleBot(constants.token)
upd = bot.get_updates()
if upd == []:
    while upd == []:
        bot.get_updates()
last_upd = upd[-1]  # последнее обновление
message = last_upd.message

# работа с файлами

# файлы сортировок
directory = 'C:/Users/power/Desktop/telebot/libs'
all_files = os.listdir(directory)
# файлы сортировок

direc = 'C:/Users/power/Desktop/telebot/libs/alg'
all_files1 = os.listdir(direc)
print(all_files, text.info[0])
# работа с файлами

# log сообщений
def log(message, answer):
    print('-' * 20)
    from datetime import datetime
    print(datetime.now())
    print(f'Сообщение: {message.text}, Ответ: {answer}, Пользователь {message.from_user.first_name}')
    print('-' * 20)

# -------markup--------
user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
btn1 = telebot.types.KeyboardButton('Сортировки')
btn2 = telebot.types.KeyboardButton('Другие алгоритмы')
user_markup.add(btn1, btn2)

sorts_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
bt1 = telebot.types.KeyboardButton('Пузырьковая сортировка')
bt2 = telebot.types.KeyboardButton('Сортировка выбором')
bt3 = telebot.types.KeyboardButton('Сортировка вставками')
bt4 = telebot.types.KeyboardButton('Сортировка методом Шелла')
bt5 = telebot.types.KeyboardButton(u'\u21A9 Назад')
sorts_markup.add(bt1, bt2, bt3, bt4, bt5)

alg_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
b1 = telebot.types.KeyboardButton('Алгоритм Евклида')
b2 = telebot.types.KeyboardButton('Вычисление факториала')
b3 = telebot.types.KeyboardButton('Двоичный (бинарный) поиск элемента')
b4 = telebot.types.KeyboardButton('Перевод из десятичной сис. в двоичную')
b5 = telebot.types.KeyboardButton('Числа Фибоначчи')
b6 = telebot.types.KeyboardButton(u'\u21A9 Назад')
alg_markup.add(b1, b2, b3, b4, b5, b6)

# -------markup--------

#обработка команд
@bot.message_handler(commands = ['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup = user_markup)
@bot.message_handler(commands = ['help'])
def handle_help(message):
    bot.send_message(message.chat.id, """
    Список команд:
/start - стартовать
/help - помощь
/alghorythms - получить код одного из алгоритмов
    """)
@bot.message_handler(commands = ['alghorythms'])
def handle_alg(message):
    pass

# обработка обычного текста
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Сортировки':
        answer = 'Вы выбрали пункт сортировки, выберите ту, код которой хотите получить'
        bot.send_message(message.chat.id, answer, reply_markup = sorts_markup)
    elif message.text == 'Пузырьковая сортировка':
        answer = text.sorts[0]
        bot.send_message(message.chat.id, answer, reply_markup = user_markup, parse_mode = "HTML")
        doc = open(directory + '/' + all_files[1], 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, doc)
        bot.send_message(message.chat.id, text.info[0], reply_markup = user_markup)
        img = open('C:/Users/power/Desktop/telebot/images/bubble.gif', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_document(message.from_user.id, img)            
    elif message.text == 'Сортировка вставками':
        answer = text.sorts[1]
        bot.send_message(message.chat.id, answer, reply_markup = user_markup, parse_mode = "HTML")
        doc = open(directory + '/' + all_files[2],'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, doc)   
        bot.send_message(message.chat.id, text.info[1], reply_markup = user_markup)
        img = open('C:/Users/power/Desktop/telebot/images/insertion.gif', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_document(message.from_user.id, img)          
    elif message.text == 'Сортировка выбором':
        answer = text.sorts[2]
        bot.send_message(message.chat.id, answer, reply_markup = user_markup, parse_mode = "HTML")
        doc = open(directory + '/' + all_files[3], 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, doc)   
        bot.send_message(message.chat.id, text.info[2], reply_markup = user_markup)     
        img = open('C:/Users/power/Desktop/telebot/images/selection.gif', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_document(message.from_user.id, img)            
    elif message.text == 'Сортировка методом Шелла':
        answer = text.sorts[3]
        bot.send_message(message.chat.id, answer, reply_markup = user_markup, parse_mode = "HTML")  
        doc = open(directory + '/' + all_files[4], 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, doc)  
        bot.send_message(message.chat.id, text.info[3], reply_markup = user_markup)   
        img = open('C:/Users/power/Desktop/telebot/images/shell.gif', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_document(message.from_user.id, img)          
        
        
    elif message.text == 'Другие алгоритмы':
        answer = 'Вы выбрали пункт "другие алгоритмы", выберите ту, код которой хотите получить'
        bot.send_message(message.chat.id, answer, reply_markup = alg_markup)        
        
    elif message.text == 'Алгоритм Евклида':
        answer = text.alg[0]
        bot.send_message(message.chat.id, answer, reply_markup = user_markup, parse_mode = "HTML") 
        doc = open(direc + '/' + all_files1[1], 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, doc)       
        bot.send_message(message.chat.id, text.info[4], reply_markup = user_markup)
    elif message.text == 'Вычисление факториала':
        answer = text.alg[1]
        bot.send_message(message.chat.id, answer, reply_markup = user_markup, parse_mode = "HTML") 
        doc = open(direc + '/' + all_files1[2], 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, doc)          
        bot.send_message(message.chat.id, text.info[5], reply_markup = user_markup)
    elif message.text == 'Двоичный (бинарный) поиск элемента':
        answer = text.alg[2]
        bot.send_message(message.chat.id, answer, reply_markup = user_markup, parse_mode = "HTML") 
        bot.send_message(message.chat.id, text.info[6], reply_markup = user_markup)
        doc = open(direc + '/' + all_files1[0], 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, doc)          
    elif message.text == 'Перевод из десятичной сис. в двоичную':
        answer = text.alg[3]
        bot.send_message(message.chat.id, answer, reply_markup = user_markup, parse_mode = "HTML") 
        bot.send_message(message.chat.id, text.info[7], reply_markup = user_markup)        
        img = open('C:/Users/power/Desktop/telebot/images/per.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_document(message.from_user.id, img)           
        doc = open(direc + '/' + all_files1[4], 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, doc)          
    elif message.text == 'Числа Фибоначчи':
        answer = text.alg[4]
        bot.send_message(message.chat.id, answer, reply_markup = user_markup, parse_mode = "HTML") 
        doc = open(direc + '/' + all_files1[3], 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, doc)          

    
    elif message.text == '\u21A9 Назад':
        answer = 'Вы перешли назад'
        bot.send_message(message.chat.id, answer, reply_markup = user_markup) 
        
    else:
        answer = 'Я не понимаю о чем вы, чтобы узнать список команд пропишите /help'
        bot.send_message(message.chat.id, answer)
    log(message, answer)

bot.polling(none_stop = True, interval = 0)
