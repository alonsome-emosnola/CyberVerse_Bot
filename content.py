import os
import nest_asyncio
import asyncio
from cyberverse_token import func
from dotenv import load_dotenv
from aiogram.utils.deep_linking import get_start_link, get_startgroup_link
from aiogram.types.message import Message
from text_generator import generate

load_dotenv()

nest_asyncio.apply()

HOLDER = generate()

coin_details = {
    "name": "CyberVerse",
    "symbol": "CBV",
    "site": "https://cyberverse.xyz",
    "decimal": 18,
    "contract_address": os.environ["CONTRACT_ADDRESS"],
    "token_supply_amount": func["total_supply"],
    "twitter": "https://twitter.com/CyberverseToken?t=fHe2QXOzPJdNZNFu7Xh7nQ&s=09",
    "telegram": "https://t.me/cyberverse_coin",
    "referral_link": f"https://t.me/cyberversebot?start={HOLDER}",
    "airdrop_amt": 1000,
    "referral_count": 0,
    "wallet_address": "",
    "bal": func["normalize"](asyncio.run(func["bal"](os.environ["ADDRESS_2"]))),
    "total_supply": func["normalize"](asyncio.run(func["total_supply"]())),
    "total_circulating": func["normalize"](asyncio.run(func["total_circulating"]()))
}


def start(name):
    """
    This is the first or start step of the bot process that begins initialization of the bot procedure, here the user initializes conversation by sending the command '/start' or '/help' to begin interaction with CBV bot.
    """
    return f"""Hello, {name} You Are Welcome To {coin_details["name"]}

    ✅Please Do The Required Tasks To Be Eligible To Get {coin_details["airdrop_amt"]}{coin_details["symbol"]} Airdrop Tokens from our total supply of {coin_details["total_supply"]}{coin_details["symbol"]}.

    🔹 <a href="{coin_details["telegram"]}">Join Our Sponsor's Airdrop Announcements Channel</a>
    🔹 <a href="{coin_details["twitter"]}">Follow Our Sponsor's Twitter</a>
    🔹 Submit Your BEP-20 Address

    📘By Participating You Are Agreeing To Centric Cash (Airdrop) Program Terms and Conditions.

    Click "🔶 Join Airdrop" to proceed
    
    🔝 Main Menu

    """

second_reply = f"""
🔹 <a href="{coin_details["telegram"]}">Join Our Sponsor's Airdrop Announcements Channell</a>

🔹 <a href="{coin_details["twitter"]}">Join Our Sponsor's Airdrop Twitter Handle</a>
"""

third_reply = f"""
Join Our Sponsor's <a href="{coin_details["twitter"]}">Twitter Account</a> (Like And Retweet Pinned Post)

Then Enter Your Twitter Username Here"""

fourth_reply = f"""
Submit Your BNB Smart Chain (BEP-20) Address Here
"""

hurray = f"""

Hurray! You Have Completed All The Tasks Successfully

Now Click On "🔶 Claim 1000 {coin_details["symbol"]}" Button
"""

successful_reg = f"""
❇️ You Have Successfully Claimed Your 1000 {coin_details["symbol"]} Bonus Tokens 

Now You Can Start Inviting Your Friends To Earn 100 {coin_details["symbol"]} Tokens For Each Referral

Wallet Address - ' '

Referral Link - {coin_details["referral_link"]}

Referral Count - {coin_details["referral_count"]}

Balance - 1000
🔶 Claim 1000 {coin_details["symbol"]} Bonus
"""