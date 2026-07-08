import requests
import time

# ===== НАСТРОЙКИ =====
BOT_TOKEN = "8602158976:AAG7HW36OfIgijBzcYf823hRgvRI1w0_6_s"

# ===== ФУНКЦИИ =====
def get_updates(offset=None):
    """Получает новые сообщения от Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    params = {"timeout": 30, "offset": offset}
    
    try:
        response = requests.get(url, params=params, timeout=35)
        return response.json().get("result", [])
    except Exception as e:
        print(f"Ошибка: {e}")
        return []

def send_message(chat_id, text):
    """Отправляет сообщение пользователю"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    
    try:
        requests.post(url, json=data, timeout=10)
    except Exception as e:
        print(f"Ошибка отправки: {e}")

# ===== ОБРАБОТКА СООБЩЕНИЙ =====
def handle_message(chat_id, text, username):
    """Обрабатывает сообщения и команды"""
    
    # Команды
    if text == "/start":
        send_message(chat_id, f"Привет, {username}! 👋\nНапиши /help для команд.")
    
    elif text == "/help":
        send_message(chat_id, """Доступные команды:
/start - Приветствие
/help - Эта справка
/time - Текущее время
/echo <текст> - Повторить текст""")
    
    elif text == "/time":
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        send_message(chat_id, f"🕐 {now}")
    
    elif text.startswith("/echo"):
        args = text.replace("/echo", "").strip()
        if args:
            send_message(chat_id, f"🔊 {args}")
        else:
            send_message(chat_id, "Напиши что-нибудь после /echo")
    
    # Обычные сообщения
    elif "привет" in text.lower():
        send_message(chat_id, "Привет! Как дела? 😊")
    
    elif "как дела" in text.lower():
        send_message(chat_id, "Норм, а у тебя? 🤖")
    
    elif "пока" in text.lower():
        send_message(chat_id, "Пока! 👋")
    
    else:
        send_message(chat_id, f"Ты написал: {text}")

# ===== ЗАПУСК БОТА =====
def main():
    print("🤖 Бот запущен...")
    print("Нажми Ctrl+C для остановки\n")
    
    last_update_id = None
    
    while True:
        try:
            updates = get_updates(last_update_id)
            
            for update in updates:
                last_update_id = update["update_id"] + 1
                
                if "message" in update:
                    msg = update["message"]
                    chat_id = msg["chat"]["id"]
                    username = msg["from"].get("first_name", "Пользователь")
                    text = msg.get("text", "")
                    
                    print(f"📩 {username}: {text}")
                    handle_message(chat_id, text, username)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            print("\n👋 Бот остановлен")
            break
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(3)

# ===== ЗАПУСК =====
if __name__ == "__main__":
    main()