import os
import re
import nest_asyncio
import asyncio
import content
import db
from cyberverse_token import func
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentType  # for reply keyboard (sends message)

from time import sleep
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.environ["CYBERVERSE_TOKEN"])
dp = Dispatcher(bot)

### add stuff here

nest_asyncio.apply()


# language selection
join_airdrop = KeyboardButton("🔶 Join Airdrop")  
lang_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(join_airdrop)

# sends welcome message after start
@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    reply = content.start(message.from_user.first_name)
    await message.answer(reply, reply_markup=lang_kb, disable_web_page_preview=True, parse_mode="HTML")

# sends help message
next_opt = KeyboardButton('🔶 Next')
back_opt = KeyboardButton('🔙 Back')
main_menu_opt = KeyboardButton('🔝 Main Menu')
en_options_kb = ReplyKeyboardMarkup(row_width=7, resize_keyboard=True, one_time_keyboard=True).add(next_opt).add(back_opt).add(main_menu_opt)

# @dp.message_handler(content_types=ContentType.TEXT)
@dp.message_handler(lambda message: message.text and "🔶 Join Airdrop" in message.text)
async def second_reply(message: types.Message):
    if message.text == "🔶 Join Airdrop":
        reply = content.second_reply
        await message.answer(reply, reply_markup=en_options_kb, disable_web_page_preview=True, parse_mode="HTML")
    else:
        reply = "Sorry, the option you selected is not available"
        await message.answer(reply, reply_markup=lang_kb, disable_web_page_preview=True, parse_mode="HTML")

cancel = KeyboardButton('🚫 Cancel')
menu2 = ReplyKeyboardMarkup(row_width=7, resize_keyboard=True, one_time_keyboard=True).add(cancel)
#### selecting what you need
@dp.message_handler(content_types=ContentType.TEXT)
async def third_reply(message: types.Message):
    if message.text == "🔶 Next":
        reply = content.third_reply
        await message.answer(reply, reply_markup = menu2, disable_web_page_preview=True, parse_mode="HTML")
    elif message.text == "🔙 Back":
        reply = content.second_reply
        await message.answer(reply, reply_markup = menu2, disable_web_page_preview=True, parse_mode="HTML")
    elif message.text == "🔝 Main Menu":
        reply = message.text
        await message.answer(reply, reply_markup = menu2, disable_web_page_preview=True, parse_mode="HTML")
    else:
        # reply = "Sorry, the option you selected is not available, please select an option from the keyboard menu"
        # await message.answer(reply, reply_markup = menu2, disable_web_page_preview=True, parse_mode="HTML")
        asyncio.run(fourth_reply(message))

@dp.message_handler(lambda message: message.text and "@emosnola" in message.text)
@dp.message_handler(content_types=ContentType.TEXT)
async def fourth_reply(message: types.Message):
    if message.text == message.text:
        reply = content.fourth_reply
        await message.answer(reply, reply_markup = menu2, disable_web_page_preview=True, parse_mode="HTML")
    else:
        asyncio.run(hurray_reply(message))

claim = KeyboardButton(f"🔶 Claim {content.coin_details['airdrop_amt']} CBV Bonus")
iandn = KeyboardButton('🎁 Invite & Earn')
balance = KeyboardButton('💰 Balance')
withdraw = KeyboardButton('✅ Withdraw')
back_opt2 = KeyboardButton('🔝 Back')
main_menu_opt2 = KeyboardButton('🔝 Main Menu')
menu3 = ReplyKeyboardMarkup(row_width=7, resize_keyboard=True, one_time_keyboard=True).add(claim).add(iandn).add(balance).add(withdraw).add(back_opt2).add(main_menu_opt2)

@dp.message_handler(content_types=ContentType.TEXT)
async def hurray_reply(message: types.Message):
    db.post_wallet({
        "name": f"{message.from_user.first_name} {message.from_user.last_name}",
        "username": message.from_user.username,
        "wallet": message.text
    })
    reply = content.hurray
    await message.answer(reply, reply_markup=menu3, disable_web_page_preview=True, parse_mode="HTML")
    asyncio.run(content_successful_reg(message))

@dp.message_handler(content_types=ContentType.TEXT)
async def content_successful_reg(message: types.Message):
    if message.text == f"🔶 Claim {content.coin_details['airdrop_amt']} CBV Bonus":
        db.post_link({
        "name": f"{message.from_user.first_name} {message.from_user.last_name}",
        "username": message.from_user.username,
        "referral_link": content.r_link
        })

        wallet = db.read_wallet({"username": message.from_user.username}, {"_id": 0, "wallet": 1})

        link = db.read_link({"username": message.from_user.username}, {"_id": 0, "referral_link": 1})

        reply = content.successful_reg(wallet, link)
        await message.answer(reply, reply_markup = menu3)
    elif message.text == '💰 Balance':
        reply = content.balance(link)
        await message.answer(reply, reply_markup = menu3)
    elif message.text == '✅ Withdraw':
        reply = content.withdraw(content.coin_details["referral_count"])
        await message.answer(reply, reply_markup = menu3)
    elif message.text == '🎁 Invite & Earn':
        reply = content.invite_and_earn(link)
        await message.answer(reply, reply_markup = menu3)
    elif message.text == '🔝 Back':
        reply = content.hurray
        await message.answer(reply, reply_markup = menu3)
    elif message.text == '🔝 Main Menu':
        reply = content.successful_reg(wallet, link)
        await message.answer(reply, reply_markup = menu3)

# this is the last line
executor.start_polling(dp)