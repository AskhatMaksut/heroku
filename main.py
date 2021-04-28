import subprocess,telebot
subprocess.call('soffice --headless --convert-to pdf:writer_pdf_Export --outdir /app *.docx',shell=True)
bot = telebot.TeleBot('1679597751:AAHfoNzsYE4mcZpBqekcjTQP1euKgSGNoks')

@bot.message_handler(content_types=['text'])
def echo_all(message):
   bot.send_document(message.chat.id, open(r'app/hello.pdf, 'rb'))


bot.polling(True)
