import telebot
import os

class BotHandler():
    def __init__(self) -> None:
        token = os.getenv('TELEGRAM_TOKEN')
        self.bot = telebot.TeleBot(token)

        print(f'init bot: {self.bot}')

        self.bot.register_message_handler(self.greet_handler, commands=['hi'])
        self.bot.register_message_handler(self.echo_message, content_types=['text'], func=lambda message: True)
    
    def pass_lambda_event(self, event):
        update = telebot.types.Update.de_json(event['body'])
        print(f'pass_lambda_event update: {update}')
        # self.bot.process_new_updates([update])
        message = update.message
        self.bot.reply_to(message, message.text)

    def greet_handler(self, message):
        print(f'greet_handler called with message text: {message.text}')
        self.bot.reply_to(message, "hello my name is IPPT Challenge Bot")

    # Handle all other messages
    def echo_message(self, message):
        print(f'echo_message called with message text: {message.text}')
        print(f'bot: {self.bot}')
        print('1')
        print('2')
        print('3')
        print('4')
        print('5')
        print(f'message: {message}')
        self.bot.reply_to(message, message.text)