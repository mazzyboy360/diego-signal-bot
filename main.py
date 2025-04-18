from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Link to your Telegram channel
CHANNEL_LINK = "https://t.me/millionariodiegosignal"

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Entrar no canal", url=CHANNEL_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "👋 *Bem-vindo ao Bot de Sinais Diego Câmara!*\n\n"
        "Entre agora no nosso canal *DIEGO CÂMARA SIGNAL ENTRADAS* para receber:\n"
        "• Sinais gratuitos todos os dias\n"
        "• Dicas VIP de trading\n"
        "• Entradas ao vivo no mercado\n\n"
        "Clique no botão abaixo para entrar:"
    )

    update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

def main():
    updater = Updater("7747993311:AAE8POMna4qHOnTkmuVn5W-1D4omi6ShIFE", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
