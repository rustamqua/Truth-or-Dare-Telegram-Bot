import constants
class Game:
    Game_Truth=list()
    Game_Dare=constants.dare_list
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

