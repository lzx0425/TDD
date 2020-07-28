import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
	def correct_pwd(self):
		the_pwd = "Iloveyou3000!"
		self.assertTrue(check_pwd(the_pwd),msg="this is the correct password")

	def wrong_pwd_short_8(self):
		the_pwd = "I<3u"
		slef.assertFalse(check_pwd(the_pwd),msg="length is too short")
	
	def wrong_pwd_greater_20(self):
		the_pwd = "Iloveyoumorethan3000times!!<3"
		self.asserTrue(check_pwd(the_pwd),msg="length is too long")
