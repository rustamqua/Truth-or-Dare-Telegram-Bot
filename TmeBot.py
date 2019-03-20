import telebot
import constants
import BotType
import random
bot= telebot.TeleBot(token=constants.token)
new=BotType.Game()
@bot.message_handler(commands=["start"])
def welcome(message):
    user_markup=telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row("/girls","/guys")
    user_markup.row("/friends","/flirt")
    user_markup.row("/adults")
    user_markup.row("/play")
    bot.reply_to(message,constants.hello,reply_markup=user_markup)
@bot.message_handler(commands=["adults"])
def adults(message):
    new.setAdults()
    bot.reply_to(message,"Adults mode setted")
@bot.message_handler(commands=["friends"])
def friends(message):
    new.setFriends()
    bot.reply_to(message,"Frinds mode setted")
@bot.message_handler(commands=["girls"])
def girls(message):
    new.setGirls()
    bot.reply_to(message,"Girls mode setted")
@bot.message_handler(commands=["guys"])
def guys(message):
    new.setGuys()
    bot.reply_to(message,"Guys mode setted")
@bot.message_handler(commands=["flirt"])
def flirt(message):
    new.setFlirt()
    bot.reply_to(message,"Flirt mode setted")
@bot.message_handler(commands=["basic"])
def basic(message):
    new.setBasic()
@bot.message_handler(commands=["play"])
def play(message):
    r=random.randrange(0,2)
    if r==0:
        r1=random.randrange(0,len(new.Game_Truth))
        bot.send_message(message.chat.id,"Truth! "+new.Game_Truth[r1])
    else:
        r1=random.randrange(0,len(new.Game_Dare))
        bot.send_message(message.chat.id,"Dare! "+new.Game_Dare[r1])

bot.polling()
