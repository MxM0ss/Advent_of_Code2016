import pdb

inputfile = open('day_4.txt')
text = inputfile.read()
split = text.split('\n')
split.pop()
real = []

alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,
'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,
'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,
'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}



for x in split:
	#organizing info
	make_up = []
	let = []
	checksum = x[-6:-1]
	raw = x[0:-7]
	data = raw
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

	#finding real rooms 
	checklist = []
	
	for x in checksum:
		checklist.append(x)
	if checklist == order:
		real.insert(0,data)

#deciphering
for x in real:
	new = ''
	numless = x[0:-3]
	shift = int(x[-3:])%26
	for y in numless:
		if y == '-':
			pass
		else:
			move = alpha[y] + shift
			if move > 26:
				move = move - 26
			new = new + list(alpha.keys())[list(alpha.values()).index(move)]
	if 'north' in new:
		print(x)


