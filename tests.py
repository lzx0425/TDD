import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
	def test1(self):
		the_pwd = ""
		self.assertFalse(check_pwd(the_pwd),msg="this is an empty password")

	def test2_correct_pwd(self):
		the_pwd = "Iloveyou3000!"
		self.assertTrue(check_pwd(the_pwd),msg="this is the correct password")

	def test_3_wrong_pwd_short_8(self):
		the_pwd = "I<3u"
		self.assertFalse(check_pwd(the_pwd),msg="length is too short")

	def test_4_wrong_pwd_greater_20(self):
		the_pwd = "Iloveyoumorethan3000times!!<3"
		self.assertFalse(check_pwd(the_pwd),msg="length is too long")
	
	def test_5_wrong_pwd_no_lower(self):
		the_pwd = "ILOVEYOU3000!"
		self.assertFalse(check_pwd(the_pwd),msg="no lower case")
	
	def test_6_wrong_pwd_no_upper(self):
		the_pwd = "iloveyou3000!"
		self.assertFalse(check_pwd(the_pwd),msg="no upper case")
		self.assertTrue(check_pwd(the_pwd),msg="no upper case")


if __name__ == '__main__':
	unittest.main()
