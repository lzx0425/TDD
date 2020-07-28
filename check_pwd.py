#def char_check(pwd):
#	dig_check = False
#	special_char = {'~','`','!','@','#','$','%','^','&','*','(',')','_','+','-','='}
#	if not any(char in special_char for char in pwd):
#		return False

#	if not any(char.islower() for char in pwd):
#		return False
#
#	if not any(char.isupper() for char in pwd):
#		return False
	
#	for char in pwd:
#		if char.isdigit():
#			dig_check = True

#	return True

def check_pwd(pwd_input):
	if len(pwd_input) > 20 or len(pwd_input) < 8:
		return False
	special_char = ['~','`','!','@','#','$','%','^','&','*','(',')','_','+','-','=']
	if not any(char in special_char for char in pwd):
		return False
	if not any(char.islower() for char in pwd):
		return False
	if not any(char.isupper() for char in pwd):
		return False
	return True
	#return char_check(pwd_input)
