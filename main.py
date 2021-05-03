import subprocess,telebot,time
bot = telebot.TeleBot('1679597751:AAHfoNzsYE4mcZpBqekcjTQP1euKgSGNoks')

@bot.message_handler(content_types=['document'])
def echo_all(message):
    file_name = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    src = file_name
    with open(r'\app\{}'.format(src), 'wb') as new_file:
        new_file.write(downloaded_file)
    subprocess.call('soffice --headless --convert-to pdf /app/{}'.format(src))
   
   
    


bot.polling(True)
