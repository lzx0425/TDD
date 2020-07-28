import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
	def test1(self):
		the_pwd = ""
		self.assertFalse(check_pwd(the_pwd),msg="this is an empty password")
		self.assertTrue(check_pwd(the_pwd),msg="this is an empty password")

	

if __name__ == '__main__':
	unittest.main()
