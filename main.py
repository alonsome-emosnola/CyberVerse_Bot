import os
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler

load_dotenv()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.effective_user)
    greeting = f"""
    👋 Hello!, @{update.effective_user.username} Welcome To CyberVerse
        
    🔥 Community Tasks

    🔰 Visit Website: https://cyberverse.xyz and connect wallet
            
    🔰 Join CyberVerse Telegram Channel

    🔰 Join Advertiser Telegram Channel

    🔰 Join CyberVerse Main Group or AITrader Second Group or CyberVerse Third Group

    🔰 Use positive words to chat in the group, otherwise you will miss this big opportunity

    ⏩ Submit your Telegram username,  Example: @username
    """
    await update.message.reply_text(greeting)

async def confirm_username(update: Update, context=ContextTypes.DEFAULT_TYPE) -> None:

    msg = f"""
    👉 Please visit following links to understand AIT project
        
    Website | CMC | Pancakeswap | Whitepaper

    🔥 AIT IDO is live: https://ait.finance
    🔥 IDO price: 1 BNB = 640,000 AIT

    🔥 AITrader was built with a strong design philosophy built on five main pillars: Simplicity, Pragmatism, Sustainability and Intelligent AI Trading.

    👏 AI Trader is based on the web3 architecture, the faster transaction processing speed will allow Farm,NFT, Staking, Dex, Metaverse and other applications have a better experience in AI Trader


    Click "NEXT" to join airdrop
        """

#bot_instance = Bot(os.environ.get("CYBERVERSE_TOKEN")).send_message(6180471148, "testing", "CHAT").send(1)

app = ApplicationBuilder().token(os.environ["CYBERVERSE_TOKEN"]).build()

app.add_handler(CommandHandler("start", hello))
app.bot(app)

app.run_polling()