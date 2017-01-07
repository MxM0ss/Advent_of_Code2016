import hashlib
import pdb

string = 'uqwqemis'
password = ''
num = 0
nums = []
#[4515059, 6924074, 8038154, 13432968, 13540621, 14095580, 14821988, 16734551] are nums from part 1

while len(password) < 8:
	hashed = hashlib.md5((string + str(num)).encode())
	if '00000' == hashed.hexdigest()[0:5]:
		password = password + hashed.hexdigest()[5]
		print(password)
		nums.append(num)
		num += 1
	else:
		if num%10000000 == 0:
			print(num)
		num += 1
print(nums)