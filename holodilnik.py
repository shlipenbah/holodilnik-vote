import logging
import yaml
from telegram.ext import Updater
from telegram.ext import CommandHandler


with open('config.yml') as config:
    params = yaml.load(config)
    updater = Updater(token=params['token'])


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def stop():
    updater.stop()


def new_vote(bot, update, args):
    usage='You should specify [vote_name] [variant1] [variant2] and so on'
    if not args:
        bot.send_message(chat_id=update.message.chat_id, text=usage)
    elif len(args) in range(3):
        bot.send_message(chat_id=update.message.chat_id, text='Does only one variant make sense? {}'.format(usage))
    else:
        confirmation="You want to create a vote {} with {} variants, don't you?".format(args[0], len(args) - 1)
        bot.send_message(chat_id=update.message.chat_id, text=confirmation)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# To add start command
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
vote_handler = CommandHandler('newvote', new_vote, pass_args=True)
stop_handler = CommandHandler('stop', updater.stop())
dispatcher.add_handler(start_handler)
dispatcher.add_handler(vote_handler)
dispatcher.add_handler(stop_handler)

# To start the bot, run
updater.start_polling()








