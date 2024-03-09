# 7193336435:AAFL7za4D1CY_RXeK2cC32GFFX-h4OIvyNY

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola, ¿en qué puedo ayudarte?')

app = ApplicationBuilder().token("7193336435:AAFL7za4D1CY_RXeK2cC32GFFX-h4OIvyNY").build()

app.add_handler(CommandHandler("hola", hello))

app.run_polling()