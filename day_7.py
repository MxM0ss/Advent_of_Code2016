import re

total = 0
with open('day_7.txt' , 'r') as raw:
	data = raw.read().split('\n')

data.pop()

def split_hypernet(x):
	normal = []
	hypernet = []
	strings = re.findall('\w+' , x)
	for y in strings:
		if strings.index(y) % 2 == 0:
			normal.append(y)
		else:
			hypernet.append(y)
	return normal , hypernet

def pattern_find(x):
	while len(x) > 3:
		if x[0] == x[3] and x[1] == x[2] and x[0] != x[1]:
			return True
		else:
			x = x[1:]
	return False

def support_TLS(x):
	broken = split_hypernet(x)
	for y in broken[1]:
		if pattern_find(y):
			return False
	for z in broken[0]:
		if pattern_find(z):
			return True
	return False

for x in data:
	if support_TLS(x):
		total += 1
print(total)






'''
import re

f = open('day_7.txt', 'r')
input = [line.strip() for line in f.readlines()]
f.close()


# Function definitions

def detect_abba(addr_part):
	"""Checks for ABBA sequence in supplied string. Returns True/False."""
	charlist = list(addr_part)
	while len(charlist) > 3:
		if (charlist[0] == charlist[3] and
			charlist[1] == charlist[2] and
			charlist[0] != charlist[1]):
			return True
		else:
			charlist.remove(charlist[0])
	
	return False # Only do this if a match not found in the above loop


def parse_address(addr):
	"""Get normal and hypernet sequences and return them in a dict."""
	address = addr
	norm_seqs = []
	hyper_seqs = []

	while len(list(address)) > 0:
		if list(address)[0] != '[':
			m = re.search('^[a-z]+', address)
			norm_seqs.append(m.group(0))
		else:
			m = re.search('\[[a-z]+\]', address)
			hyper_seqs.append(m.group(0))
		
		address = list(address)
		for n in range(0, len(m.group(0))):
			address.remove(address[0])
		address = "".join(address)

	return {'norm_seqs': norm_seqs, 'hyper_seqs': hyper_seqs}


def supports_tls(addr):
	"""Make sure the hypernets don't have any ABBAs, and at least one ABBA can
	be found in the normal address sequences. Return True if so.
	"""
	address_parts = parse_address(addr)
	for seq in address_parts['hyper_seqs']:
		if detect_abba(seq):
			return False
	for seq in address_parts['norm_seqs']:
		if detect_abba(seq):
			return True


def main():
	tls_addresses = []
	for address in input:
		if supports_tls(address):
			tls_addresses.append(address)
	for x in tls_addresses:
		print(x)
	print('{} addresses support TLS.'.format(len(tls_addresses)))


# Main section

main()'''