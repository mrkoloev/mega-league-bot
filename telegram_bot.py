import telegram


def send_msg(msg, chat_id: str, token: str, parse_mode='HTML'):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg, parse_mode=parse_mode, disable_web_page_preview=True)


def send_document(document, chat_id: str, token: str):
    bot = telegram.Bot(token=token)
    bot.send_document(chat_id=chat_id, document=document)


def send_img(img_path, chat_id: str, token: str, url):
    bot = telegram.Bot(token=token)
    bot.send_photo(photo=open(file=img_path, mode='rb'), chat_id=chat_id, caption=url)
