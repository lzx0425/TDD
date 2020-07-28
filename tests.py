import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):

	def empty_pwd(self):
		the_pwd = ""
		self.assertFalse(check_pwd(the_pwd),msg="this is an empty password")

	def correct_pwd(self):
		the_pwd = "Iloveyou3000!"
		self.assertTrue(check_pwd(the_pwd),msg="this is the correct password")

	def wrong_pwd_short_8(self):
		the_pwd = "I<3u"
		slef.assertFalse(check_pwd(the_pwd),msg="length is too short")
	
	def wrong_pwd_greater_20(self):
		the_pwd = "Iloveyoumorethan3000times!!<3"
		self.assertFalse(check_pwd(the_pwd),msg="length is too long")

	def wrong_pwd_no_lower(self):
		the_pwd = "ILOVEYOU3000!"
		self.assertFalse(check_pwd(the_pwd),msg="no lower case")

	def wrong_pwd_no_upper(self):
		the_pwd = "iloveyou3000!"
		self.assertFalse(check_pwd(the_pwd),msg="no upper case")

if __name__ == '__main__':

	unittest.main()
