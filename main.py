from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# Установи токен телеграм-бота
TELEGRAM_BOT_TOKEN = '5332606660:AAFhidzUlldBwNJAO74mkk2AsQ0V7_2ERak'
updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)

# Установи ключ OpenAI
OPENAI_API_KEY = 'ваш_ключ'
openai.api_key = OPENAI_API_KEY

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, давай пообщаемся.')

# Обработчик текстовых сообщений
def handle_text(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    # Здесь можешь использовать GPT для обработки user_input
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    bot_reply = response.choices[0].text.strip()
    update.message.reply_text(bot_reply)

# Добавление обработчиков команд
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

# Запуск бота
updater.start_polling()
updater.idle()
