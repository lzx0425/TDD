def check_pwd(pwd_input):
	if len(pwd_input) > 20 or len(pwd_input) < 8:
		return False
	return char_check(pwd_input)
