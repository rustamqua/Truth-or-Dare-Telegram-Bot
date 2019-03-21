import unittest
import BotType
import constants
class MyTest(unittest.TestCase):
    def test_girls(self):
        temp=BotType.Game()
        temp.setGirls()
        result=temp.getTruth()
        self.assertEqual(result,constants.truth_girls)
    def test_guys(self):
        temp=BotType.Game()
        temp.setGuys()
        result=temp.getTruth()
        self.assertEqual(result,constants.truth_guys)
    def test_adults(self):
        temp=BotType.Game()
        temp.setAdults()
        result=temp.getTruth()
        self.assertEqual(result,constants.truth_adults)
    def test_flirt(self):
        temp=BotType.Game()
        temp.setFlirt()
        result=temp.getTruth()
        self.assertEqual(result,constants.truth_flirt)
    def test_friends(self):
        temp=BotType.Game()
        temp.setFriends()
        result=temp.getTruth()
        self.assertEqual(result,constants.truth_frineds)
    def test_basic(self):
        temp=BotType.Game()
        result=temp.getTruth()
        self.assertEqual(result,constants.truth_halal)
if __name__=="__main__":
    unittest.main()

