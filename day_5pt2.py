import hashlib
import pdb
import time

string = 'uqwqemis'
password = ['','','','','','','','']
num = 0
nums = []

while '' in password:
	fake = ['','','','','','','','']
	hashed = hashlib.md5((string + str(num)).encode())
	if '00000' == hashed.hexdigest()[0:5]:
		if hashed.hexdigest()[5] in '1234567890':
			if int(hashed.hexdigest()[5]) > 7:
				pass
			if int(hashed.hexdigest()[5]) < 8:
				if password[int(hashed.hexdigest()[5])] == '':
					password[int(hashed.hexdigest()[5])] = hashed.hexdigest()[6]
					nums.append(num)
				else:
					pass
		else:
			pass
		num += 1
	else:
		if num%1000 == 0:
			for x in range(len(password)):
				if password[x] != '':
					fake[x] = password[x]
				else:
					fake[x] = hashed.hexdigest()[x]
			print(''.join(fake))
		if num%1000000 == 0:
			print(num)
			time.sleep(.25)
		num += 1
print('finished')
print(password)
print(nums)
for x in nums:
	hashed = hashlib.md5((string + str(x)).encode())
	print(hashed.hexdigest())
pdb.set_trace()