import subprocess,telebot
bot = telebot.TeleBot('1679597751:AAHfoNzsYE4mcZpBqekcjTQP1euKgSGNoks')

@bot.message_handler(content_types=['document'])
def echo_all(message):
    file_name = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    src = file_name
    with open(r'app\{}'.format(src), 'wb') as new_file:
        new_file.write(downloaded_file)
    subprocess.call('soffice --headless --convert-to pdf /app/{}'.format(src),shell=True)
    if src[-4:] == 'docx':
        b = src[:-4]
        src = b + 'pdf'
    else:
        b = src[:-3]
        src = b + 'pdf'
    uis_pdf = open('/app/{}'.format(src), 'rb')
    bot.send_document(message.chat.id, uis_pdf)
    uis_pdf.close()
    import os,time
    time.sleep(10)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), str(src))
    os.remove(path)
    


bot.polling(True)
