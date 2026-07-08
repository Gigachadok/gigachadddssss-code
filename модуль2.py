import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Включим логирование для отслеживания ошибок
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен вашего бота (получите у @BotFather)
BOT_TOKEN = "8602158976:AAG7HW36OfIgijBzcYf823hRgvRI1w0_6_s"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! 👋\n"
        f"Я простой бот. Вот что я умею:\n"
        f"/start - показать это сообщение\n"
        f"/help - получить помощь\n"
        f"Просто напиши мне что-нибудь, и я отвечу!"
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Доступные команды:\n"
        "/start - начать работу\n"
        "/help - показать эту справку\n"
        "/echo <текст> - повторю твоё сообщение\n"
        "/caps <текст> - напишу текст заглавными буквами\n\n"
        "Также я отвечаю на обычные сообщения!"
    )

# Команда /echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Получаем текст после команды
    if context.args:
        text = ' '.join(context.args)
        await update.message.reply_text(f"Эхо: {text}")
    else:
        await update.message.reply_text("Напиши что-нибудь после /echo")

# Команда /caps
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        text = ' '.join(context.args)
        await update.message.reply_text(text.upper())
    else:
        await update.message.reply_text("Напиши текст после /caps")

# Обработчик обычных текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()
    
    # Простые ответы на ключевые слова
    if "привет" in message_text or "здравствуй" in message_text:
        await update.message.reply_text("Привет! Как дела? 😊")
    elif "как дела" in message_text:
        await update.message.reply_text("У меня всё отлично! А у тебя? 🤖")
    elif "пока" in message_text:
        await update.message.reply_text("До свидания! Буду ждать тебя снова 👋")
    elif "спасибо" in message_text:
        await update.message.reply_text("Пожалуйста! Рад помочь 😊")
    else:
        await update.message.reply_text(
            f"Ты написал: {update.message.text}\n\n"
            f"Используй /help, чтобы узнать мои команды!"
        )

# Обработчик ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Ошибка: {context.error}")
    if update and update.effective_message:
        await update.effective_message.reply_text("Произошла ошибка. Попробуйте позже.")

def main():
    # Создаём приложение
    app = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("caps", caps))
    
    # Обработчик текстовых сообщений (не команд)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Регистрируем обработчик ошибок
    app.add_error_handler(error_handler)

    # Запускаем бота
    print("Бот запущен...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()