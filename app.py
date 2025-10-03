from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your bot token
BOT_TOKEN = "7842720027:AAGrey5_ViPAGluUhn3QBsEqrQT9MA85C4k"

# Define the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey, how do you do?")

def main():
    # Create the bot application
    app = Application.builder().token(BOT_TOKEN).build()

    # Add handler for /start
    app.add_handler(CommandHandler("start", start))

    # Run the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
