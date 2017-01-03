import pdb

inputfile = open('day_4.txt')
text = inputfile.read()
split = text.split('\n')
split.pop()
total = 0

alpha = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,
'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,
'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,
'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

for x in split:
	#organizing info
	make_up = []
	let = []
	checksum = x[-6:-1]
	raw = x[0:-7]
	number = raw[-3:]
	for char in '1234567890-':
		if char in raw:
			raw = raw.replace(char, '')
			letters = ''.join(sorted(raw))
	for char in letters:
			let.append(char)
	for char in let:
		if char not in make_up:
			make_up.append(char)
		else:
			pass

	#sorting info
	order = []
	while len(order) < 5:
		letter = make_up[0]
		for x in make_up:
			if let.count(x) > let.count(letter):
				letter = x
			elif let.count(x) == let.count(letter):
				if alpha[x] < alpha[letter]:
					letter = x
				else:
					pass
			else:
				pass
		order.append(letter)
		make_up.remove(letter)

	#comparing checksum to 
	checklist = []
	for x in checksum:
		checklist.append(x)
	if checklist == order[0:5]:
			total = total + int(number)

print(total)