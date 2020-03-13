import logging
import glob
import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PATH = './aneks_vk/*.txt'
TOKEN = 'TOKEN'
# Reads API token from local file
with open('./private', 'r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text
    (
    'ОГОГО ЁБАНЫЙ РОТ! Я - искусственный интеллект, мне скормили более 3000'\
    ' анеков! Напиши /banek, чтобы получить мой авторский prikol.'\
    )
    
def help(update, context):
    update.message.reply_text('Напиши мне /banek, чтобы ржака')


def echo(update, context):
    update.message.reply_text('Я тебя не понимаю. Напиши /help, чтобы узнать список доступных комманд')


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def get_banek(update, context):
    '''
    This func won't work without local storage of jokes
    The storage name defined in PATH variable
    '''
    files = glob.glob(PATH)
    # Takes random joke number from available range
    anek_number = random.randint(0, files.__len__())
    with open(files[anek_number], 'r') as f:
        update.message.reply_text('Пока мне мозги не подвезли и я не умею придумывать'\
            ' новые ржачьки, так что держи один из тех анеков, что я знаю:\n\n\n' + f.read())


def main():
    logger.warning('STARTING...')
    updater = Updater(TOKEN, use_context=True)

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