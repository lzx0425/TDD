import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
	def test1(self):
		the_pwd = ""
		self.assertFalse(check_pwd(the_pwd),msg="this is an empty password")

	def test2_correct_pwd(self):
		the_pwd = "Iloveyou3000!"
		self.assertTrue(check_pwd(the_pwd),msg="this is the correct password")
		self.assertFalse(check_pwd(the_pwd),msg="this is the correct password")


if __name__ == '__main__':
	unittest.main()
