from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Токен бота (замените на свой)
TOKEN = 7510774892:AAGmj0AQ89Uey8Q_qBYbVoC5VuFPJKeataE

# Функция, которая вызывается при команде /start
def start(update: Update, context: CallbackContext) -> None:
    # Создаем кнопки для меню
    buttons = [
        ["🎮 Играть", "📊 Профиль"],  # Первая строка кнопок
        ["🆘 Помощь", "⚙️ Настройки"]  # Вторая строка
    ]
    
    # Создаем меню с кнопками
    reply_markup = ReplyKeyboardMarkup(
        buttons, 
        resize_keyboard=True,  # Кнопки подстраиваются под размер экрана
        one_time_keyboard=False  # Меню не исчезнет после нажатия
    )
    
    # Отправляем сообщение с меню
    update.message.reply_text(
        "Добро пожаловать в 'Завод Котиков'! 🐱\n"
        "Выберите действие:",
        reply_markup=reply_markup
    )

# Функция для обработки нажатий на кнопки
def button_click(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if text == "🎮 Играть":
        update.message.reply_text("Игра запускается... 🚀")
    elif text == "📊 Профиль":
        update.message.reply_text("Ваш профиль: ...")
    elif text == "🆘 Помощь":
        update.message.reply_text("Это игра-кликер. Нажимайте кнопки и зарабатывайте монеты!")
    elif text == "⚙️ Настройки":
        update.message.reply_text("Настройки бота...")

# Основная функция
def main():
    # Создаем бота и передаем ему токен
    updater = Updater(TOKEN)
    
    # Получаем "диспетчер" для регистрации обработчиков
    dp = updater.dispatcher
    
    # Регистрируем обработчики команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, button_click))
    
    # Запускаем бота
    updater.start_polling()
    print("Бот запущен! 🚀")
    updater.idle()  # Бот будет работать, пока не остановите вручную

if __name__ == "__main__":
    main()