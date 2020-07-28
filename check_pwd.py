def char_check(pwd):
	special_char = {'~','`','!','@','#','$','%','^','&','*','(',')','_','+','-','='}
	if not any(char in special_char for char in pwd):
		return False

	return True

def check_pwd(pwd_input):
	if len(pwd_input) > 20 or len(pwd_input) < 8:
		return False
	return char_check(pwd_input)
