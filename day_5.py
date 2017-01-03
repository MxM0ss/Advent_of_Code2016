import hashlib
import pdb

string = 'uqwqemis'
password = ''
num = 0

while len(password) < 8:
	hashed = hashlib.md5((string + str(num)).encode())
	if '00000' == hashed.hexdigest()[0:5]:
		password = password + hashed.hexdigest()[5]
		print(password)
		num += 1
	else:
		if num%10000000 == 0:
			print(num)
		num += 1
		