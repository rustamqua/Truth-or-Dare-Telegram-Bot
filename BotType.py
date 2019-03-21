import constants
import telebot
class Game:
    def __init__(self):
        self.Game_Truth=constants.truth_halal
        self.Game_Dare=constants.dare_list
        self.bot=telebot.TeleBot(constants.token)   
    def setFriends(self):
        self.Game_Truth=constants.truth_frineds
    def setBasic(self):
        self.Game_Truth=constants.truth_halal
    def setGirls(self):
        self.Game_Truth=constants.truth_girls
    def setAdults(self):
        self.Game_Truth=constants.truth_adults
    def setFlirt(self):
        self.Game_Truth=constants.truth_flirt
    def setGuys(self):
        self.Game_Truth=constants.truth_guys
    def getTruth(self):
        return self.Game_Truth
    def getDare(self):
        return self.Game_Dare
    def startPolling(self):
        self.bot.polling()
    def getBot(self):
        return self.bot
class Facade:
    def __init__(self):
        self.bot=Game()
    def start(self):
        self.bot.startPolling()
    def getBot(self):
        return self.bot.getBot()
    