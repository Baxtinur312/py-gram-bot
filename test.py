from pygrambot import Updater, MessageHandler, CommandHandler, CallbackQueryHandler

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

def start_command(update):
    message = update.message
    user_name = message.from_user.first_name
    
    welcome_text = f"Salom {user_name}!\n\n"
    welcome_text += "Bu pygrambot kutubxonasi orqali yaratilgan bot!\n\n"
    welcome_text += "Mavjud komandalar:\n"
    welcome_text += "• /help - Yordam\n"
    welcome_text += "• /info - Ma'lumot"
    
    updater.bot.send_message(message.chat.id, welcome_text)

def help_command(update):
    message = update.message
    
    help_text = "pygrambot yordam:\n\n"
    help_text += "Bu kutubxona o'zbekistonlik dasturchi tomonidan yaratilgan!\n\n"
    help_text += "Xususiyatlari:\n"
    help_text += "✅ Oddiy va tushunarli\n"
    help_text += "✅ O'zbek tilida hujjatlar\n"
    help_text += "✅ Barcha asosiy funksiyalar"
    
    updater.bot.send_message(message.chat.id, help_text)

def info_command(update):
    message = update.message
    
    info_text = f"Xabar ma'lumotlari:\n\n"
    info_text += f"Foydalanuvchi: {message.from_user.first_name}\n"
    info_text += f"User ID: {message.from_user.id}\n"
    info_text += f"Chat ID: {message.chat.id}\n"
    info_text += f"Xabar ID: {message.message_id}"
    
    updater.bot.send_message(message.chat.id, info_text)

def handle_text_messages(message):
    text = message.text.lower()
    
    if text == "salom":
        updater.bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}!")
    else:
        updater.bot.send_message(message.chat.id, f"Siz yozdingiz: {message.text}")

def handle_photos(message):
    response_text = "Ajoyib rasm!\n"
    response_text += "Rahmat rasmingiz uchun!"
    
    updater.bot.send_message(message.chat.id, response_text)

if __name__ == "__main__":
    print("pygrambot ishga tushmoqda...")
    
    updater = Updater(BOT_TOKEN)
    
    updater.dispatcher.add_handler(CommandHandler('start', start_command))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('info', info_command))
    
    updater.dispatcher.add_handler(
        MessageHandler(handle_photos, content_types=['photo'])
    )
    
    updater.dispatcher.add_handler(
        MessageHandler(handle_text_messages, content_types=['text'])
    )
    
    updater.start_polling()