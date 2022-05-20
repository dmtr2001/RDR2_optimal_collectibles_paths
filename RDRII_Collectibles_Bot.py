# -*- coding: cp1251 -*-
from os import waitpid
import telebot;
from telebot import types
import datetime

bot = telebot.TeleBot('5348879862:AAHetIidhaH3iKbiYN2xE0xzICWpRZL1ITg');

cups = list()
pentacles = list()
swords = list()
wands = list()

userid = list()

@bot.message_handler(commands=['start'])    
def Start(message):
    global cups
    global pentacles
    global swords
    global wands
    global userid
    if message.from_user.id not in userid:
        userid.append(message.from_user.id)
        cups.append(0)
        pentacles.append(0)
        swords.append(0)
        wands.append(0)
        s = "New user was added.   User: " + "(" + str(message.from_user.id) + ")"
        if (message.from_user.first_name != None):
            s += " "
            s += message.from_user.first_name
        if (message.from_user.last_name != None):
            s += " "
            s += message.from_user.last_name
        if (message.from_user.username != None):
            s += " ("
            s += message.from_user.username
            s += ")"
        print(s)
        
    bot.send_message(message.from_user.id, "This bot shows you the best routes to collect tarot cards in Red Dead Online")
    
    AskAboutSets(message)


@bot.message_handler(content_types=['text'])
def Reply(message):
    global cups
    global pentacles
    global swords
    global wands
    
    if message.text == "Сhoose another cards":
            AskAboutSets(message)
    
    if message.from_user.id not in userid:
        bot.send_message(message.from_user.id, "Unfortunately we have to start over")
        AskAboutSets(message)
    else: 
        if message.text == "Add Cups":
            cups[userid.index(message.from_user.id)] = 1
            ChooseSets(message)
        if message.text == "Exclude Cups":
            cups[userid.index(message.from_user.id)] = 0
            ChooseSets(message)

        if message.text == "Add Pentacles":
            pentacles[userid.index(message.from_user.id)] = 1
            ChooseSets(message)
        if message.text == "Exclude Pentacles":
            pentacles[userid.index(message.from_user.id)] = 0
            ChooseSets(message)

        if message.text == "Add Swords":
            swords[userid.index(message.from_user.id)] = 1
            ChooseSets(message)
        if message.text == "Exclude Swords":
            swords[userid.index(message.from_user.id)] = 0
            ChooseSets(message)

        if message.text == "Add Wands":
            wands[userid.index(message.from_user.id)] = 1
            ChooseSets(message)
        if message.text == "Exclude Wands":
            wands[userid.index(message.from_user.id)] = 0
            ChooseSets(message)

        if message.text == "Next":
            ChooseDay(message)
        if message.text == "Day 1":
            Answer(message, 1)
        if message.text == "Day 2":
            Answer(message, 2)
        if message.text == "Day 3":
            Answer(message, 3)
        if message.text == "Day 4":
            Answer(message, 4)
        if message.text == "Day 5":
            Answer(message, 5)
        if message.text == "Day 6":
            Answer(message, 6)
        
        if message.text == "Choose anoher day":
            ChooseDay(message)

def AskAboutSets(message):
    global cups
    global pentacles
    global swords
    global wands
    global userid
    
    if message.from_user.id not in userid:
        userid.append(message.from_user.id)
        cups.append(0)
        pentacles.append(0)
        swords.append(0)
        wands.append(0)
 
        s = "New user was added.   User: (" + str(message.from_user.id) + ")"
        if (message.from_user.first_name != None):
            s += " "
            s += message.from_user.first_name
        if (message.from_user.last_name != None):
            s += " "
            s += message.from_user.last_name
        if (message.from_user.username != None):
            s += " ("
            s += message.from_user.username
            s += ")"
        print(s)

    cups[userid.index(message.from_user.id)] = 0
    pentacles[userid.index(message.from_user.id)] = 0
    swords[userid.index(message.from_user.id)] = 0
    wands[userid.index(message.from_user.id)] = 0

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    key_cups = types.KeyboardButton("Add Cups")
    key_pentacles = types.KeyboardButton("Add Pentacles")
    key_swords = types.KeyboardButton("Add Swords")
    key_wands = types.KeyboardButton("Add Wands")
    keyboard.add(key_cups, key_pentacles, key_swords, key_wands)

    question = "What cards you want to collect?";
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


def ChooseSets(message):
    global cups
    global pentacles
    global swords
    global wands
    global userid

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    if cups[userid.index(message.from_user.id)] == 1:
        bot.send_message(message.from_user.id, text="Cups included")
        key_cups = types.KeyboardButton("Exclude Cups")
    else:
        key_cups = types.KeyboardButton("Add Cups")

    if pentacles[userid.index(message.from_user.id)] == 1:
        bot.send_message(message.from_user.id, text="Pentacles included")
        key_pentacles = types.KeyboardButton("Exclude Pentacles")
    else:
        key_pentacles = types.KeyboardButton("Add Pentacles")

    if swords[userid.index(message.from_user.id)] == 1:
        bot.send_message(message.from_user.id, text="Swords included")
        key_swords = types.KeyboardButton("Exclude Swords")
    else:
        key_swords = types.KeyboardButton("Add Swords")

    if wands[userid.index(message.from_user.id)] == 1:
        bot.send_message(message.from_user.id, text="Wands included")
        key_wands = types.KeyboardButton("Exclude Wands")
    else:
        key_wands = types.KeyboardButton("Add Wands")

    if (cups[userid.index(message.from_user.id)] == 1 or pentacles[userid.index(message.from_user.id)] == 1 or swords[userid.index(message.from_user.id)] == 1 or wands[userid.index(message.from_user.id)] == 1):
        key_next = types.KeyboardButton("Next")
        keyboard.add(key_cups, key_pentacles, key_swords, key_wands, key_next)
    else:
        keyboard.add(key_cups, key_pentacles, key_swords, key_wands)

    question = "Something else?";
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

def ChooseDay(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    key_day1 = types.KeyboardButton("Day 1")
    key_day2 = types.KeyboardButton("Day 2")
    key_day3 = types.KeyboardButton("Day 3")
    key_day4 = types.KeyboardButton("Day 4")
    key_day5 = types.KeyboardButton("Day 5")
    key_day6 = types.KeyboardButton("Day 6")
    keyboard.add(key_day1, key_day2, key_day3, key_day4, key_day5, key_day6)

    bot.send_message(message.from_user.id, text="Choose day", reply_markup=keyboard)

def Answer(message, day):
    global cups
    global pentacles
    global swords
    global wands
    have_image = 0
    count = 0
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True);

    key_wait = types.KeyboardButton("I'm waiting...")
    keyboard.add(key_wait)
    bot.send_message(message.from_user.id, text="Give me a sec...", reply_markup=keyboard)

    filename = "C:\RDRII_bot\ "
    filename = filename[:-1]

    if cups[userid.index(message.from_user.id)] == 1:
        filename += "cups"
        count += 1
    if pentacles[userid.index(message.from_user.id)] == 1:
        if count > 0:
            filename += "_"
        filename += "pentacles"
        count += 1
    if swords[userid.index(message.from_user.id)] == 1:
        if count > 0:
            filename += "_"
        filename += "swords"
        count += 1
    if wands[userid.index(message.from_user.id)] == 1:
        if count > 0:
            filename += "_"
        filename += "wands"
        count += 1

    filename = filename + "_day" + str(day) + ".jpg"
    today = datetime.datetime.today()
    s = "(" + str(message.from_user.id) + ")"
    if (message.from_user.first_name != None):
        s += " "
        s += message.from_user.first_name
    if (message.from_user.last_name != None):
        s += " "
        s += message.from_user.last_name
    if (message.from_user.username != None):
        s += " ("
        s += message.from_user.username
        s += ")"
    s += " want "
    s += filename
    s += "     "
    s += today.strftime("%d-%m-%Y  %H:%M:%S")
    print(s)
    
    try:
        image  =  open(filename, 'rb')
        bot.send_document(message.from_user.id, image)
        have_image = 1
        today = datetime.datetime.today()
        s = "(" + str(message.from_user.id) + ")"
        if (message.from_user.first_name != None):
            s += " "
            s += message.from_user.first_name
        if (message.from_user.last_name != None):
            s += " "
            s += message.from_user.last_name
        if (message.from_user.username != None):
            s += " ("
            s += message.from_user.username
            s += ")"
        s += " receive "
        s += filename
        s += "     "
        s += today.strftime("%d-%m-%Y  %H:%M:%S")
        print(s)
    except Exception:
        have_image = 0
        today = datetime.datetime.today()
        s = "(" + str(message.from_user.id) + ")"
        if (message.from_user.first_name != None):
            s += " "
            s += message.from_user.first_name
        if (message.from_user.last_name != None):
            s += " "
            s += message.from_user.last_name
        if (message.from_user.username != None):
            s += " ("
            s += message.from_user.username
            s += ")"
        s += " did not receive "
        s += filename
        s += "     "
        s += today.strftime("%d-%m-%Y  %H:%M:%S")
        print(s)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    key_collect = types.KeyboardButton("Сhoose another cards")
    key_choose_day = types.KeyboardButton("Choose anoher day")
    keyboard.add(key_collect, key_choose_day)

    if have_image == 1:
        bot.send_message(message.from_user.id, "Collect it!", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Something go wrong...", reply_markup=keyboard)

bot.polling(none_stop = True, interval = 0)