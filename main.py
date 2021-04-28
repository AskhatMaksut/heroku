import subprocess,telebot
subprocess.call('soffice --headless --convert-to pdf:writer_pdf_Export --outdir /app *.docx',shell=True)
bot = telebot.TeleBot('1679597751:AAHfoNzsYE4mcZpBqekcjTQP1euKgSGNoks')

@bot.message_handler(content_types=['text'])
def echo_all(message):
   if message.text == 'Hello':
       uis_pdf = open('app/hello.pdf', 'rb')
       bot.send_document(message.chat.id, uis_pdf)
       uis_pdf.close()


bot.polling(True)
