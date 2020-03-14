import logging
import glob
import random
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = str(os.environ.get('TOKEN'))
PORT = int(os.environ.get('PORT', '9349'))
APP_NAME = str(os.environ.get('APP_NAME'))


def start(update, context):
    update.message.reply_text('ОГОГО ЁБАНЫЙ РОТ! Я - искусственный интеллект,'
    'мне скормили более 3000 анеков! Напиши /banek, чтобы получить мой авторский'
    'prikol.')


def help(update, context):
    update.message.reply_text('Напиши мне /banek, чтобы ржака')


def echo(update, context):
    update.message.reply_text('Я тебя не понимаю. Напиши /help, чтобы узнать список доступных комманд')


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def get_banek(update, context):
    update.message.reply_text('Пока мне мозги не подвезли и я не умею придумывать ржомбу')


def main():
    logger.warning('STARTING...')
    updater = Updater(TOKEN, use_context=True)
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(APP_NAME, TOKEN))

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('banek', get_banek))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
