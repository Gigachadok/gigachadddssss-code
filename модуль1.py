import requests
import time
import json
from threading import Thread

# Токен бота (получи у @BotFather)
BOT_TOKEN = "8602158976:AAG7HW36OfIgijBzcYf823hRgvRI1w0_6_s"
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

# Хранилище пользователей (в реальном проекте используй БД)
user_data = {}

def get_updates(offset=None):
    """Получает обновления от Telegram API"""
    url = URL + "getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()["result"]

def send_message(chat_id, text):
    """Отправляет сообщение"""
    url = URL + "sendMessage"
    params = {"chat_id": chat_id, "text": text}
    requests.get(url, params=params)

def handle_start(chat_id, username):
    """Обработчик команды /start"""
    text = f"Привет, {username}! 👋\nЯ простой бот на чистом Python.\nНапиши /help для списка команд."
    send_message(chat_id, text)

def handle_help(chat_id):
    """Обработчик команды /help"""
    text = """📋 Доступные команды:
/start - начать работу
/help - показать это сообщение
/time - показать текущее время
/echo <текст> - повторю твоё сообщение
/caps <текст> - напишу текст заглавными
/calc <число> <операция> <число> - калькулятор

Также я отвечаю на обычные сообщения!"""
    send_message(chat_id, text)

def handle_time(chat_id):
    """Показывает текущее время"""
    import datetime
    now = datetime.datetime.now().strftime("%H:%M:%S")
    send_message(chat_id, f"🕐 Текущее время: {now}")

def handle_echo(chat_id, text):
    """Повторяет текст"""
    args = text.replace("/echo", "").strip()
    if args:
        send_message(chat_id, f"🔊 Эхо: {args}")
    else:
        send_message(chat_id, "Напиши что-нибудь после /echo")

def handle_caps(chat_id, text):
    """Переводит текст в верхний регистр"""
    args = text.replace("/caps", "").strip()
    if args:
        send_message(chat_id, args.upper())
    else:
        send_message(chat_id, "Напиши текст после /caps")

def handle_calc(chat_id, text):
    """Простой калькулятор"""
    try:
        # Удаляем команду /calc
        expression = text.replace("/calc", "").strip()
        # Безопасно вычисляем выражение
        result = eval(expression, {"__builtins__": {}}, {})
        send_message(chat_id, f"🧮 Результат: {result}")
    except:
        send_message(chat_id, "❌ Ошибка! Используй формат: /calc 5 + 3")

def handle_message(chat_id, text):
    """Обрабатывает обычные сообщения"""
    text_lower = text.lower()
    
    if "привет" in text_lower or "здравствуй" in text_lower:
        send_message(chat_id, "Привет! Как дела? 😊")
    elif "как дела" in text_lower:
        send_message(chat_id, "У меня всё отлично! А у тебя? 🤖")
    elif "пока" in text_lower:
        send_message(chat_id, "До свидания! 👋")
    elif "спасибо" in text_lower:
        send_message(chat_id, "Пожалуйста! Рад помочь 😊")
    elif "как тебя зовут" in text_lower:
        send_message(chat_id, "Я простой Telegram бот!")
    else:
        send_message(chat_id, f"Ты написал: {text}\n\nНапиши /help для списка команд")

def main():
    """Основной цикл бота"""
    print("🤖 Бот запущен...")
    last_update_id = None
    
    while True:
        try:
            updates = get_updates(last_update_id)
            
            for update in updates:
                # Получаем ID последнего обновления
                last_update_id = update["update_id"] + 1
                
                # Проверяем наличие сообщения
                if "message" in update:
                    message = update["message"]
                    chat_id = message["chat"]["id"]
                    
                    # Получаем имя пользователя
                    username = message["from"].get("first_name", "Пользователь")
                    
                    # Проверяем текст сообщения
                    if "text" in message:
                        text = message["text"]
                        
                        # Обрабатываем команды
                        if text.startswith("/start"):
                            handle_start(chat_id, username)
                        elif text.startswith("/help"):
                            handle_help(chat_id)
                        elif text.startswith("/time"):
                            handle_time(chat_id)
                        elif text.startswith("/echo"):
                            handle_echo(chat_id, text)
                        elif text.startswith("/caps"):
                            handle_caps(chat_id, text)
                        elif text.startswith("/calc"):
                            handle_calc(chat_id, text)
                        else:
                            handle_message(chat_id, text)
            
            time.sleep(1)  # Пауза между запросами
            
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()