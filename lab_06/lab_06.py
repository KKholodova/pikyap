from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Функция, которая запускается при вызове команды /start
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Кнопка 1", callback_data='button1'),
            InlineKeyboardButton("Кнопка 2", callback_data='button2'),
        ],
        [InlineKeyboardButton("Кнопка 3", callback_data='button3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

# Функция для обработки нажатий на кнопки
def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    query.edit_message_text(f"Вы нажали на кнопку: {query.data}")

def main() -> None:
    updater = Updater("6858904745:AAFc9OWOr8x5cyvJwaRpoEQ-1HIJqBsHGUc")
    dispatcher = updater.dispatcher

    # Обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))

    # Обработчик нажатий на кнопки
    dispatcher.add_handler(CallbackQueryHandler(button_click))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
