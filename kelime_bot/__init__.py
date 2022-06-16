from time import sleep
from pyrogram import Client
import logging


# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)





# Hesap
API_ID = "16102648"
API_HASH = "378a73e340eb634cf67c8c42bafa9f37"
TOKEN = "5515833309:AAEqq4CIwdmZUxT_Ll5OyHdTyTTy52KhyRM" 
USERNAME = "5249642922"




# BOT CLIENTİ
bot = Client(
    ":memory:",
    API_ID, "16102648"
    API_HASH, "378a73e340eb634cf67c8c42bafa9f37"
    bot_token=TOKEN, "5515833309:AAEqq4CIwdmZUxT_Ll5OyHdTyTTy52KhyRM" 
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
    )


# Oyun Verileri
oyun = {}


# rating
rating = {}





# !!!!!!!!!!!!!! DEĞİŞTİR KESİNLİKLE !!!!!!!!!!!!!!!!
#      SAHİBİN USER ID'Sİ
OWNER_ID = 5249642922

